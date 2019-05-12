# -*- coding: utf-8 -*-  
# !! 必须hook pydub.silence的split_on_silence, 否则程序报错

from cmdCaller import formatChange
from cmdCaller import subprocessCaller
from fileHelper import get_file_content
from pydub import AudioSegment
from pydub.silence import split_on_silence
from fileHelper import moveFile

import requests
from srtMakeHelper import *
from aip import AipSpeech
import os
import subprocess

#用作及时关闭多余连接，否则会http连接过多而网络拥塞
s = requests.session()


#使用个人使用的百度识别api

APP_ID = '15925422'
API_KEY = 'j7hGczEvpfdAlRi8CIajUaFE'
SECRET_KEY = 'TLMjIMceRe16X0flNi1DacPQycEfhyZy'



def split(chunk,min_silence_len,length_limit,silence_thresh,level = 0):

    print(' *'*20,'拆分开始',' *'*20)

    if len(chunk)>length_limit:
        print('Level: %d 执行拆分'%(level))

        (chunk_splits,NonSilencePair) = split_on_silence(chunk,min_silence_len=min_silence_len,silence_thresh=silence_thresh)
       
        print(' *'*20, '拆分结束，返回段数:',len(chunk_splits),' *'*20)
        
        return (chunk_splits,NonSilencePair)
    
    print(' *'*20,'拆分失败，音段过短',' *'*20)
    
    exit()

def wavToPcm(wavName):
    #wav -> pcm
    getpcm = 'ffmpeg -i ./chunks/%s -ar 16000 -ac 1 -acodec pcm_s16le -f s16le ./chunks/%s.pcm'%(wavName,wavName[:-4])
    
    subprocess.call(getpcm,shell = True)

def recognizePCM(pcmName_PREFIX):

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    #及时关闭多余连接
    s.keep_alive = False

    #识别参数必须配置
    respose = client.asr(get_file_content('./chunks/%s.pcm'%pcmName_PREFIX), 'pcm', 16000, {
    'dev_pid': 1536,
    })

    if 'result' in respose.keys():
        return (respose['result'][0])
    else :
        return ""

def getSRT(inputFileName):

    #总流程
    print(' *'*20,'识别语音生成字幕开始',' *'*20)


    #1：从视频中提取转为wav
    name = formatChange(inputFileName,'wav')

    #2:载入wav文件
    sound = AudioSegment.from_wav(name)

    #3：设置参数准备进入拆分
    silence_thresh=-50      # 小于-50dBFS以下的为静默
    min_silence_len=300     # 静默超过300毫秒则拆分
    length_limit=10*1000    # 拆分后每段不得超过10s
    abandon_chunk_len=300    # 放弃小于300毫秒的段

    #4：拆分
    (chunks,NonSilencePair) = split(sound,min_silence_len,length_limit,silence_thresh)

    #5:舍弃过短的片段
    Index = list(range(len(chunks)))[::-1]
    for i in Index:
        if(len(chunks[i]) < abandon_chunk_len):
            print("放弃%d"%i)
            chunks.pop(i)
            NonSilencePair.pop(i)

    #5：保存拆分结果
    # (1) 创建文件夹
    if not os.path.exists('./chunks'):os.mkdir('./chunks')
    namef,namec = os.path.splitext(name)
    namec = namec[1:]

    # (2) 保存所有分段&做语音识别，保存在content内
    Lesson_content =[]
    total_num = len(chunks)
    for i in range(total_num):
        new = chunks[i]
        save_name = '%s_%04d.%s'%(namef,i,namec)
        new.export('./chunks/'+save_name, format=namec)
        wavToPcm(save_name)
        response = recognizePCM(save_name[:-4])
        Lesson_content.append(response)
        print('Chunk ID: ','%04d'%i, ' length:%d'%(len(new)))

    print(' *'*20,'保存结束',' *'*20)

    
    #6识别语音并且写入srt
    TimeStamps = [{"Begin":x[0],"End":x[1]} for x in NonSilencePair]
    GenerateSrtFormatFile(TimeStamps,Lesson_content)


    #将tmp文件移走
    moveFile(name,'./tmp/%s'%name)

    print(' *'*20,'成功生成srt',' *'*20)



