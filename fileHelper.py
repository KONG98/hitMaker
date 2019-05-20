# -*- coding: utf-8 -*-  
import os
import shutil


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 移动文件
def moveFile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s does not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(srcfile, dstfile)
        print("move %s -> %s" % (srcfile, dstfile))

       


# 读取目标文件夹的所有文件的文件名
def get_imgFile():
    for root, dirs, files in os.walk('img'):
        img = [(str(root) + "/" + str(i)) for i in files]
        return img


# 更改目标下的所有文件名，以Index标序
def renameFile(folderName):
    index = 0
    for root, dirs, files in os.walk(folderName):
        for i in files:
            namef, namec = os.path.splitext(i)
            namec = namec[1:]
            dst = '%d.%s' % (index, namec)
            index += 1
            os.rename((str(root) + "/" + str(i)), (str(root) + "/" + str(dst)))

# 删除目标下的所有文件
def removeAllFile(folderName):
    for root, dirs, files in os.walk(folderName):
        for i in files:
            namef, namec = os.path.splitext(i)
            namec = namec[1:]
            os.remove((str(root) + "/" + str(i)))

def resizeAllImg():
    from cv2 import cv2 as cv2
    imgs = get_imgFile()
    y, x = cv2.imread(imgs[0]).shape[0:2]
    y = int(y / 2)
    x = int(x / 2)

    for name in imgs:
        img = cv2.imread(name)
        img = cv2.resize(img, (x, y))
        print(name)
        cv2.imwrite(name, img, [cv2.IMWRITE_JPEG_QUALITY, 30])
