# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 13:03
# @Author  : lazerliu
# @File    : xml2voc.py
import os
import random

# ==================������Ҫ�޸ĵĵط�=====================================#
#g_root_path = "/home/leon/lsx/yoloV4/darknet-master/VOCdevkit/VOC2020/"
g_root_path = "data/VOCdevkit/VOC2007/"
xmlfilepath = "Annotations"  # ��ע�ļ����·��
saveBasePath = "ImageSets/Main/"  # ImageSets��Ϣ����·��
trainval_percent = 0.9
train_percent = 0.7
# ==================������Ҫ�޸ĵĵط�=====================================#

os.chdir(g_root_path)
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
xml_list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(xml_list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("train  size", tr)
ftrainval = open(saveBasePath + "trainval.txt", "w")
ftest = open(saveBasePath + "test.txt", "w")
ftrain = open(saveBasePath + "train.txt", "w")
fval = open(saveBasePath + "val.txt", "w")

for i in xml_list:
    name = total_xml[i][:-4] + "\n"
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()