# coding=utf-8

import pymysql
import MySQLdb
import random
from collections import defaultdict

influencer = '../data/influencer'
output_file1 = '../data/id_fo'
output_file2 = '../data/id_fa_sample'
output_file3 = '../data/user_check'
id_fo = '../data/id_fo'
id_fa_sample = '../data/id_fa_sample'
user_attr = '../data/user_attr'


def gen_id_fo(path1, path2):
    fo_dict = {}
    user_list = []
    with open(path1, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n')
            row = row.split('\t')
            user_list.append(row[0])
    try:
        conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
        cur = conn.cursor()
        cnt = 0
        for u in user_list:
            cnt += 1
            cur.execute('Select fo from fo_table where id = %s' % u)
            res = cur.fetchall()
            fo_dict[u] = res[0][0]
            if cnt % 100 == 0:
                print(cnt)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    with open(path2, 'w') as write_f:
        for item in fo_dict:
            write_f.write('%s:%s\n' % (item, fo_dict[item]))


def gen_id_fa_sample(path1, path2, path3):
    fa_sample_dict = defaultdict(list)
    user_list = []
    with open(path1, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n')
            row = row.split('\t')
            user_list.append(row[0])
    try:
        conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
        cur = conn.cursor()
        cnt = 0
        for u in user_list:
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            cur.execute('Select fa from fa_table where id = %s' % u)
            res = cur.fetchall()
            for e in res[0][0].split('\t'):
                # 随机选取0.1%的粉丝
                rnd = random.random()
                if rnd <= 0.0001:
                    fa_sample_dict[u].append(e)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    with open(path2, 'w') as write_f:
        for item in fa_sample_dict:
            write_f.write(item)
            write_f.write(':')
            for e in fa_sample_dict[item]:
                write_f.write('%s\t' % e)
            write_f.write('\n')
    # 保存待爬取的用户
    user_check = set()
    for u in fa_sample_dict:
        for e in fa_sample_dict[u]:
            if e not in user_check:
                user_check.add(e)
    with open(path3, 'w') as write_f:
        for u in user_check:
            write_f.write(u)
            write_f.write('\n')


def create_db(path1, path2, path3):
    dict1 = defaultdict(list)
    with open(path1, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n')
            row = row.split('\t')
            dict1[row[0]].append(row[1])
            dict1[row[0]].append(row[2])
            dict1[row[0]].append(row[3])
    dict2 = {}
    with open(path2, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n')
            row = row.split(':')
            dict2[row[0]] = row[1]
    dict3 = {}
    sample_num = {}
    with open(path3, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n')
            row = row.split(':')
            dict3[row[0]] = row[1]
            sample_num[row[0]] = str(len(row[1]))
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS bigv_table")
        cur.execute("Create table bigv_table(id int primary key, uid longtext, fos longtext, fas longtext, sample_num \
                    longtext, fo longtext, fa_sample longtext) engine=myisam")
        cnt = 0
        for key in dict1:
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            cur.execute('INSERT INTO bigv_table values (%s, %s, %s, %s, %s, %s, %s)',
                        (key, dict1[key][0], dict1[key][1], dict1[key][2], sample_num[key], dict2[key], dict3[key]))
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


def create_fa_db(path):
    dict1 = defaultdict(list)
    with open(path, 'r', encoding='utf-8') as read_file:
        cnt1 = 0
        for row in read_file:
            cnt1 += 1
            if cnt1 % 100000 == 0:
                print(cnt1)
            row = row.strip('\n').split(',')
            s = ','.join(row[1:])
            dict1[row[0]] = s
    print('Starting create DB...')
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata',
                           use_unicode=True, charset="utf8")
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS fa_sample_table")
        cur.execute("Create table fa_sample_table(id int primary key, uid longtext, time longtext, fos longtext, \
                    fas longtext, statuses_count longtext, verified longtext, gender longtext, urank longtext, \
                    mbrank longtext, location longtext) engine=myisam")
        cnt2 = 0
        for key in dict1:
            cnt2 += 1
            if cnt2 % 100000 == 0:
                print(cnt2)
            s = dict1[key].split(',')
            if len(s) == 10:
                cur.execute('Insert into fa_sample_table values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                            (key, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9]))
            else:
                cur.execute('Insert into fa_sample_table (id, uid) values (%s, %s)', (key, s[0]))
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    # gen_id_fo(influencer, output_file1)
    # gen_id_fa_sample(influencer, output_file2, output_file3)
    # create_db(influencer, id_fo, id_fa_sample)
    create_fa_db(user_attr)

