import cv2
from moviepy.video.fx.speedx import speedx
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import *
from fileHelper import get_imgFile


class tkMaker:

    clip = ''

    def __init__(self, clipName=None):
 
        if clipName!=None:
            self.clip = VideoFileClip(clipName)

    def loadClip(self, clipName):
        if not os.path.exists(clipName):
            print('Error:%s does not exist' % clipName)
            return
        self.clip = VideoFileClip(clipName)

    def writeClip(self, outputVideoName):
        if os.path.exists(outputVideoName):
            print('Error:%s has been existed' % outputVideoName)
            return
        self.clip.write_videofile(outputVideoName)

    # run接口
    def run(self):
        pass


class tkHit_Speed(tkMaker):
    START = 0
    M = 1  # 加速的视频段落长
    speedRate = 5
    breakPoints = []

    def __init__(self, M, speedRate, breakPoints, clipName):
        super(tkHit_Speed, self).__init__( clipName)
        self.M = M
        self.speedRate = speedRate
        self.breakPoints = breakPoints

    def run(self,outputVideoName):
        # 对加速点迭代加速
        BgmName='BGM/model2-BGM.wav'
        for breakPoint in self.breakPoints:
            print(' *' * 12, '正在处理:', breakPoint, ' *' * 12)
            END = self.clip.end

            clipFirst = self.clip.subclip(self.START, breakPoint - self.M / self.speedRate)
            clipMiddle = speedx(
                self.clip.subclip(breakPoint - self.M / self.speedRate, breakPoint - self.M / self.speedRate + self.M),
                factor=self.speedRate)
            clipLast = self.clip.subclip(breakPoint - self.M / self.speedRate + self.M, END)

            self.clip = concatenate_videoclips([clipFirst,
                                                clipMiddle,
                                                clipLast])

        length = 0
        sound = AudioFileClip(BgmName)

        if self.clip.end < sound.end:
            length = self.clip.end
            sound = sound.subclip(0, length)
        else:
            length = sound.end
            self.clip = self.clip.subclip(0, length)

        self.clip = self.clip.set_audio(sound)
        self.writeClip(outputVideoName)


class tkHit_ImgSeq(tkMaker):
    imgs = get_imgFile()
    durations = []

    def __init__(self, clipName, durations):
        super(tkHit_ImgSeq, self).__init__( clipName)
        self.durations = durations

    def run(self,outputVideoName):
        length = 0
        BgmName='BGM/model1-BGM.wav'
        # 截取使img和durations同等长度
        if len(BgmName) != len(self.durations):
            length = min(len(BgmName), len(self.durations))
            self.durations = self.durations[0:length]
            imgs = imgs[0:length]

        # 将视频和BGM也截取相同的长度
        self.clip = ImageSequenceClip(imgs, durations=durations)
        sound = AudioFileClip(BgmName)

        if self.clip.end < sound.end:
            length = self.clip.end
            sound = sound.subclip(0, length)
        else:
            length = sound.end
            self.clip = self.clip.subclip(0, length)

        self.clip = self.clip.set_audio(sound)
        self.writeClip(outputVideoName)


from tikTokMaker import *
#model1
durations=[]
for i in range(0,10):
    durations.append(0.5)
for i in range(0,29):
    durations.append(0.1)
durations.append(1)
durations.append(0.7)
durations.append(0.2)
durations.append(0.7)

static_ImgSeq = tkHit_ImgSeq(durations=durations,clipName=None)

#model2

breakPoints = [0.12,0.22,1.02,1.22,2.02,2.15,3.02,3.15,4.15,4.20,5.13,6.20,
                    7.07,8.05,9.17,10.00,11.0,12.10,12.30,15.10,16.00]

static_tkHit_Speed  = tkHit_Speed(clipName=None,M = 1, speedRate = 5,breakPoints = breakPoints)