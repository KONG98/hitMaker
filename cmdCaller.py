import subprocess
# -*- coding: utf-8 -*-  
import os

def formatChange(inputFileName,outPutFileFormat,floder=None):

    if not os.path.exists('./afterFormatChange'):
        os.mkdir('./afterFormatChange')


    namef,namec = os.path.splitext(inputFileName)

    if floder ==None:
        outputFileName = './%s.%s'%(namef,outPutFileFormat)
    else:
        outputFileName = './%s/%s.%s'%(floder,namef,outPutFileFormat)

    cmd = 'ffmpeg -i %s %s'%(inputFileName,outputFileName)
    response = subprocess.call(cmd,shell = True)

    return outputFileName



def subprocessCaller(cmd):
    response = subprocess.call(cmd,shell = True)


def embedSRT(videoName,SrtName):
    if not os.path.exists(videoName):
        print('Error:%s does not exist'%videoName)
        return

    namef,namec = os.path.splitext(videoName)
    outputFileName = namef + str('_with_SRT')  + namec
    cmd = 'ffmpeg -i %s -vf subtitles=%s %s'%(videoName,SrtName,outputFileName)
    response = subprocess.call(cmd,shell = True)


    

