import os
import re
import shutil
filename = "~/radar/radar_reflect_data_2017/REFdata/"
filelist = os.listdir(filename)
for file in filelist:
    if re.match(r"cappi_ref_\d+_500_0.ref",file):
        shutil.copy(filename+"/"+file,"2017_500/")