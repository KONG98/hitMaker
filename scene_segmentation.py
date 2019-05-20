from cv2 import cv2 as cv2
import operator
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import sys


class SceneSegmt:
    def __init__(self):
        pass

    def __smooth(self, x, window_len=13, window='hanning'):
        print(len(x), window_len)

        s = np.r_[2 * x[0] - x[window_len:1:-1],
                  x, 2 * x[-1] - x[-1:-window_len:-1]]

        if window == 'flat':  # moving average
            w = np.ones(window_len, 'd')
        else:
            w = getattr(np, window)(window_len)
        y = np.convolve(w / w.sum(), s, mode='same')
        return y[window_len - 1:-window_len + 1]

    class __Frame:
        def __init__(self, id, diff):
            self.id = id
            self.diff = diff

        def __lt__(self, other):
            if self.id == other.id:
                return self.id < other.id
            return self.id < other.id

        def __gt__(self, other):
            return other.__lt__(self)

        def __eq__(self, other):
            return self.id == other.id and self.id == other.id

        def __ne__(self, other):
            return not self.__eq__(other)

    def __rel_change(self, a, b):
        x = (b - a) / max(a, b)
        print(x)
        return x

    def process(self, inputfile, outputpath, thresh=0.75):
        print(sys.executable)
        # Setting fixed threshold criteria
        USE_THRESH = True
        # fixed threshold value
        THRESH = thresh
        # Setting fixed threshold criteria
        USE_TOP_ORDER = False
        # Setting local maxima criteria
        USE_LOCAL_MAXIMA = False
        # Number of top sorted frames
        NUM_TOP_FRAMES = 50

        # Video path of the source file
        videopath = inputfile
        # Directory to store the processed frames
        dir = outputpath
        # smoothing window size
        len_window = int(50)

        print("target video :" + videopath)
        print("frame save directory: " + dir)
        # load video and compute diff between frames
        cap = cv2.VideoCapture(str(videopath))
        curr_frame = None
        prev_frame = None
        frame_diffs = []
        frames = []
        success, frame = cap.read()
        i = 0
        while (success):
            luv = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            curr_frame = luv
            if curr_frame is not None and prev_frame is not None:
                # logic here
                diff = cv2.absdiff(curr_frame, prev_frame)
                diff_sum = np.sum(diff)
                diff_sum_mean = diff_sum / (diff.shape[0] * diff.shape[1])
                frame_diffs.append(diff_sum_mean)
                frame = self.__Frame(i, diff_sum_mean)
                frames.append(frame)
            prev_frame = curr_frame
            i = i + 1
            success, frame = cap.read()
        cap.release()

        keyframe_id_set = set()
        if USE_TOP_ORDER:
            # sort the list in     # compute keyframe descending order
            frames.sort(key=operator.attrgetter("diff"), reverse=True)
            for keyframe in frames[:NUM_TOP_FRAMES]:
                keyframe_id_set.add(keyframe.id)
        if USE_THRESH:
            print("Using Threshold")
            for i in range(1, len(frames)):
                if (self.__rel_change(np.float(frames[i - 1].diff), np.float(frames[i].diff)) >= THRESH):
                    keyframe_id_set.add(frames[i].id)
        if USE_LOCAL_MAXIMA:
            print("Using Local Maxima")
            diff_array = np.array(frame_diffs)
            sm_diff_array = self.__smooth(diff_array, len_window)
            frame_indexes = np.asarray(argrelextrema(sm_diff_array, np.greater))[0]
            for i in frame_indexes:
                keyframe_id_set.add(frames[i - 1].id)

            plt.figure(figsize=(40, 20))
            plt.locator_params(numticks=100)
            plt.stem(sm_diff_array)
            plt.savefig(dir + 'plot.png')

        # save all keyframes as image
        cap = cv2.VideoCapture(str(videopath))
        fps = cap.get(cv2.CAP_PROP_FPS)  # 获取原视频的帧率

        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 获取原视频帧的大小

        i = 1
        j = 1
        videoWriter = cv2.VideoWriter('./output/' + str(j) + '.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                      fps, size)  # 新视频保存路径和参数

        success, frame = cap.read()
        idx = 0
        while (success):
            videoWriter.write(frame)  # 写入“新视频”

            if idx in keyframe_id_set:
                j = j + 1
                videoWriter = cv2.VideoWriter('./output/' + str(j) + '.avi',
                                              cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)  # 新视频保存路径和参数
                keyframe_id_set.remove(idx)
            idx = idx + 1
            success, frame = cap.read()
        cap.release()


if __name__ == '__main__':
    ss = SceneSegmt()
    ss.process('input.mp4', './output/', 0.9, 1)
