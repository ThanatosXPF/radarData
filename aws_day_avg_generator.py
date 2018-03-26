import numpy as np
import os


def load_aws(file_path):
    num = int(file_path[-8:-4])
    aws = np.fromfile(file_path, dtype=np.float, sep=" ").reshape(num, 5)
    total = 0.0
    for line in aws:
        if line[4] == -99.:
            num -= 1
            continue
        total += line[4]
    # print total
    return num, total


def get_day_avg(hour_list, path):
    num = 0
    total = 0.0
    for hour in hour_list:
        n, t = load_aws(os.path.join(path, hour))
        total += t
        num += n
    return total / num


def write(day_list, rain_list):
    print rain_list
    f = open("gd_rainy_days_2017.txt", "w")
    for i in range(len(day_list)):
        line = "2017" + day_list[i] + ", " + \
            str("%.2f" % rain_list[i]) + "\n"
        f.writelines(line)
    f.close()


if __name__ == '__main__':
    file_path = 'AWSrain2017'
    day_list = []
    rain_list = []
    for dir in os.listdir(file_path):
        day = dir[4:8]
        # print day
        hour_list = []
        for doc in os.listdir(os.path.join(file_path, dir)):
            if len(doc) > 21:
                hour_list.append(doc)
        # print hour_list
        avg = get_day_avg(hour_list, os.path.join(file_path, dir))
        day_list.append(str(day))
        rain_list.append(avg)
    write(day_list, rain_list)
