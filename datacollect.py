import os
import re
import shutil
import numpy as np
'''
filename = "/home/thanatos/Documents/radar_reflect_data_2017/REFdata/"
filelist = os.listdir(filename)
def find500():
    for file in filelist:
        if re.match(r"cappi_ref_\d+_500_0.ref",file):
            shutil.copy(filename+"/"+file,"2017_500/")
def find3500():
    for file in filelist:
        if re.match(r"cappi_ref_\d+_3500_0.ref",file):
            shutil.copy(filename+"/"+file,"2017_3500/")



def countMonth():
   list = []
   for file in filelist:
       month = file[14:18]
       if month not in list:
           list.append(month)
   print(list.sort())
   print(len(list))


'''


def grabSomeData():
    file_path = '2017_3500'
    filelist = os.listdir(file_path)
    for file in filelist:
        if "20170501" in file:
            shutil.copy(os.path.join(file_path, file), "20170501_500")


def classify_AWS():
    aws_dir = "AWSrain2017"
    dirs = os.listdir(aws_dir)
    for dir in dirs:
        if dir[4:8] <= "0601" and dir[4:8] >= "0401":
            shutil.copytree(os.path.join(aws_dir, dir), "aws2017_0405/" + dir)


def getTraindata():
    rafar_dir = "2017_3500"
    aws_dir = "AWSTypes/output"
    aws_days = os.listdir(aws_dir)
    for aws_day in aws_days:
        day = aws_day[:8]


def radarAnalyze():
    X = []
    Y = []
    aws_dir = "aws2017_0405"
    aws_dirs = os.listdir(aws_dir)
    radar_path = "2017_2500"
    radar_files = os.listdir(radar_path)
    for aws_hour in aws_dirs:
        hours = os.listdir(os.path.join(aws_dir, aws_hour))
        path = os.path.join(aws_dir, aws_hour)
        for hour in hours:
            if len(hour) <= 20:
                path = os.path.join(path, hour)
                hour = hour[8:17]
                for file in radar_files:
                    if hour in file:
                        x, y = getConbineData(loadref(file), loadaws(path))
                        X.extend(x)
                        Y.extend(y)
    X = np.array(X).reshape((len(X),1))
    Y = np.array(Y).reshape((len(Y),1))

    np.save("X.npy",X)
    np.save("Y.npy",Y)


def loadref(file):
    image = np.fromfile("2017_2500/" + file, dtype=np.uint8).reshape(700, 900)
    image[np.where(image == 125)] = 0
    image[np.where(image <= 15)] = 0
    image[np.where(image > 80)] = 0
    image = image * 3 + 5
    return image


def loadaws(file):
    aws = np.fromfile(file, dtype=np.uint32, sep=" ")
    return aws


def getConbineData(image, aws):
    X = []
    Y = []
    for line in aws:
        x = line[1]
        y = line[2]
        rain = line[4]
        factor = image[x][y]
        X.append(rain)
        Y.append(factor)
    return X, Y


# grabSomeData()
# find3500()
#classify_AWS()
radarAnalyze()