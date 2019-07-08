# coding=utf-8
from collections import defaultdict

bigv_path = '../data/verified_type'
activity_path = '../data/bigv/2018_07_01'
output_path = '../data/bigv/vt_fans_activity/'

type_dict = defaultdict(list)
activity_dict = {}


def load_bigv(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split(',')
            type_dict[row[2]].append(row[0])


def load_activity(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split('\t')
            activity_dict[row[0]] = row[1]


def stat_vt_activity():
    for key1 in type_dict:
        with open(output_path+key1, 'w') as write_file:
            for e in type_dict[key1]:
                write_file.write(activity_dict[e])
                write_file.write('\n')


if __name__ == '__main__':
    load_bigv(bigv_path)
    load_activity(activity_path)
    stat_vt_activity()
