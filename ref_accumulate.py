import os
import pandas as pd
from datetime import datetime
import numpy as np

def datelist(beginDate, endDate):
    date_l=[datetime.strftime(x,'%Y-%m-%d %H:%M') for x in list(pd.date_range(start=beginDate, end=endDate,freq = 'H'))]
    return date_l

def collect():
    path = "2017_2500"
    out_path = "2017_2500_hour_accumulate"
    refs = os.listdir(path)
    date_list = pd.date_range("20170401","20170601",freq="H").strftime("%Y%m%d%H").tolist()
    for hour in date_list:
        image = np.zeros(630000,dtype = np.uint16).reshape(700,900)
        print hour
        for ref in refs:
            if ref.find(hour) !=- 1:
                print "hit"
                image_ref = np.fromfile(os.path.join(path,ref),dtype=np.uint8).reshape(700,900)
                image_ref[np.where(image_ref == 125)] = 0
                image_ref[np.where(image_ref <= 15)] = 0
                image_ref[np.where(image_ref > 80)] = 0
                image += image_ref
                refs = filter(lambda x:x!=ref,refs)
        # test(test_path = out_path+"/"+hour+"_2500.npy")
        np.save(out_path+"/"+hour+"00_2500.npy",image)
        test(test_path = out_path+"/"+hour+"00_2500.npy")

def test(test_path = "2017_2500_hour_accumulate/201705210000_2500.npy"):
    
    image = np.load(test_path)
    print "test result:"+str(len(image[np.where(image != 0)]))

collect()
test()
