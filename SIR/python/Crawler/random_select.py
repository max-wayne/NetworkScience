# coding=utf-8
import math
import random

weibo_k_path = 'D:/Projects/Pycharm/SIR/Data/Info_stat/WeiboK_correlation'
user_info_path = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user_info'
dict_N = {}
dict_M = {}


def init():
    for i in range(16):
        for j in range(18):
            dict_N[(i, j)] = 0


def stat_weibo_k(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.strip('\n')
            row = row.split('\t')
            m = math.log(int(row[0]), 2)
            n = math.log(int(row[1]), 3)
            dict_N[(math.ceil(m), math.ceil(n))] += int(row[2])
    with open('./data/kin_kout_N', 'w') as write_handle:
        for key in dict_N:
            write_handle.write('%s\t%s\n' % (key, dict_N[key]))


def random_sampling(path):
    for i in range(16):
        for j in range(18):
            dict_M[(i, j)] = set()
    with open(path, 'r') as read_handle:
        cnt = 0
        for row in read_handle:
            cnt += 1
            if cnt % 1000000 == 0:
                print(cnt/1000000)
            row = row.strip('\n')
            row = row.split('\t')
            uid = row[1]
            kin = int(row[2])
            if len(row) == 4:
                kout = int(row[3])
            else:
                kout = 1
            m = math.ceil(math.log(kin, 2))
            n = math.ceil(math.log(kout, 3))
            if len(dict_M[(m, n)]) < 1000:
                if dict_N[(m, n)] >= 1000:
                    rnd = random.random()
                    if rnd <= 1000/dict_N[(m, n)]:
                        dict_M[(m, n)].add(uid)
                else:
                    dict_M[(m, n)].add(uid)
    with open('./data/random_sample', 'w') as write_handle:
        for key in dict_M:
            write_handle.write(str(key))
            write_handle.write('\t')
            for e in dict_M[key]:
                write_handle.write(e)
                write_handle.write('\t')
            write_handle.write('\n')
    for key in dict_M:
        path = './data/sample/' + 'uid' + key
        with open(path, 'w') as write_handle:
            for e in dict_M[key]:
                write_handle.write(e)
                write_handle.write('\n')


if __name__ == '__main__':
    init()
    stat_weibo_k(weibo_k_path)
    random_sampling(user_info_path)
