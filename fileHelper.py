# -*- coding: utf-8 -*-  
import os
import shutil

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:    
        return fp.read()

#移动文件
def moveFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("%s does not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    
        if not os.path.exists(fpath):
            os.makedirs(fpath)                
        shutil.move(srcfile,dstfile)         
        print ("move %s -> %s"%( srcfile,dstfile))

moveFile('video.wav','./tmp/video.wav')