from tikTokMaker import tkMaker


def getSubClip(videoName, startTime, endTime, outputName):
    tmpTkMaker = tkMaker('', '')
    tmpTkMaker.loadClip(videoName)
    tmpTkMaker.clip = tmpTkMaker.clip.subclip(startTime, endTime)
    tmpTkMaker.writeClip(outputName)
