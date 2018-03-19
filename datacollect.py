import os
import re
import shutil
import numpy as np
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
def grabSomeData():
    file_path = '2017_3500'
    filelist = os.listdir(file_path)
    for file in filelist:
        if "20170501" in file:
            shutil.copy(os.path.join(file_path,file),"20170501_500")

def radarAnalyze():
    pass
#grabSomeData()
find3500()
