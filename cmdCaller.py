import subprocess
# -*- coding: utf-8 -*-  
import os


def formatChange(inputFileName, outPutFileFormat, floder=None, mode=None):
    if not os.path.exists('./afterFormatChange'):
        os.mkdir('./afterFormatChange')

    inputFileName_pure = ''
    if mode != None:
        inputFileName_pure = inputFileName.split('/')[-1:][0]
    else:
        inputFileName_pure = inputFileName

    namef, namec = os.path.splitext(inputFileName_pure)

    if floder == None:
        outputFileName = './%s.%s' % (namef, outPutFileFormat)
    else:
        outputFileName = './%s/%s.%s' % (floder, namef, outPutFileFormat)

    cmd = 'ffmpeg -i %s %s' % (inputFileName, outputFileName)
    response = subprocess.call(cmd, shell=True)

    return outputFileName


def subprocessCaller(cmd):
    response = subprocess.call(cmd, shell=True)


def embedSRT(videoName, SrtName):
    
    
    tmp = videoName.split('/')[-1:][0]
    workStation = videoName[0:len(videoName)-len(tmp)]
    namef, namec = os.path.splitext(tmp)
    outputFileName = str(workStation)  + namef + str('_with_SRT') + namec
    cmd = 'ffmpeg -i %s -vf subtitles=%s %s' % (videoName, SrtName, outputFileName)
    response = subprocess.call(cmd, shell=True)
    return (outputFileName)

if __name__ =='__main__':
    videoName = 'C:/Users/HP/Desktop/code/hitMaker-new/hitMaker/media/video.mp4'
    embedSRT(videoName,'subtitle.srt')