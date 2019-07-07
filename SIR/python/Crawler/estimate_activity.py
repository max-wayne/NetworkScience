# coding=utf-8
import time
import re
import os

zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
inputfile = '../data/sample_whole_graph/'
start_time = time.mktime(time.strptime('2016-08-01', '%Y-%m-%d'))
L = []


def estimate_activity(path):
    if os.path.getsize(path):
        with open(path, 'r') as read_handle:
            num = 0
            cnt = 0
            for row in read_handle:
                num += 1
                if 'none' not in row and 'NoneType' not in row:
                    # print(num)
                    row = row.strip('\n')
                    row = row.split(',')
                    flag = zh_pattern.search(row[1])
                    if flag or len(row[1]) == 5:
                        cnt += 1
                    elif start_time <= time.mktime(time.strptime(row[1], '%Y-%m-%d')):
                        cnt += 1
        return cnt/num
    else:
        return 0.0


if __name__ == '__main__':
    dict = {}
    for i in range(16):
        for j in range(18):
            print(i, j)
            path = inputfile + 'uid_' + str(i) + '_' + str(j)
            if os.path.isfile(path):
                dict[(i, j)] = estimate_activity(path)
            else:
                dict[(i, j)] = 0.0
    with open('../data/activity_2016_08_01_T', 'w') as write_handle:
        for i in range(16):
            for j in range(18):
                write_handle.write(str(dict[(i, j)]))
                write_handle.write('\t')
            write_handle.write('\n')
