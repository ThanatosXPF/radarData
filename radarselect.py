import shutil
import os
def selectHour():
    radar_path = "2017_2500"
    files = os.listdir(radar_path)
    for file in files:
        if file[20:22] == "00":
            shutil.copy(os.path.join(radar_path,file),"2017_2500_hour")
selectHour()
