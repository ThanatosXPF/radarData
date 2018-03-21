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
    print("aws_dir : "+ str(aws_dirs[:5]))
    radar_path = "2017_2500"
    radar_files = os.listdir(radar_path)
    print("radar_file : " + str(radar_files[:5]))

    total = len(aws_dirs)
    i = 0.0

    for aws_hour in aws_dirs:

        print(aws_hour)

        hours = os.listdir(os.path.join(aws_dir, aws_hour))
        path = os.path.join(aws_dir, aws_hour)
        # print(path)
        #print("radar_file : " + str(hours[:5]))
        for hour in hours:
            if len(hour) >= 21:
                # print(hour)
                path2 = os.path.join(path, hour)
                hour = hour[8:16]
                # print(path2)
                print(hour)
                for file in radar_files:
                    # print(file)
                    if file[14:22] == hour:
                        # print(hour)
                        # print file
                        # print(path2)
                        print("find correlative radar!")
                        x, y = getConbineData(loadref(file), loadaws(path2))
                        X.extend(x)
                        Y.extend(y)

    X = np.array(X).reshape((len(X),1))
    Y = np.array(Y).reshape((len(Y),1))

    print(X[:100])
    # np.savetxt("X.txt",X)
    # np.savetxt("Y.txt",Y)
    # X.tofile("X")
    # Y.tofile("Y")
    np.save("X.npy",X)
    np.save("Y.npy",Y)

def loadref(file):
    image = np.fromfile("2017_2500_hour/" + file, dtype=np.uint8).reshape(700, 900)
    image[np.where(image == 125)] = 0
    image[np.where(image <= 15)] = 0
    image[np.where(image > 80)] = 0
    image = image * 3 + 5
    return image


def loadaws(file):
    num = int(file[-8:-4])
    # print(num)
    aws = np.fromfile(file, dtype=np.float, sep=" ").reshape(num,5)
    # print(aws[:5])
    return aws


def getConbineData(image, aws):
    X = []
    Y = []
    for line in aws:
        x = int(line[1])
        y = int(line[2])
        rain = line[4]
        factor = image[y][x]
        if rain == -99.0:
            continue
        X.append(rain)
        Y.append(factor)
    return X, Y


# grabSomeData()
# find3500()
#classify_AWS()
radarAnalyze()
#loadaws("aws2017_0405/2017041108-2017041111/AWS_201704110800_2309.txt")
