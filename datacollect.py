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
def countMonth():
    list = []
    for file in filelist:
        month = file[14:18]
        if month not in list:
            list.append(month)
    print(list)
    print(len(list))

countMonth()
