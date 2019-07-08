# coding=utf-8
import math
import pymysql
from collections import defaultdict


bigv_path = '../data/influencer'
'''
output_file1 = '../data/bigv/ko_fans_fans/'
output_file2 = '../data/bigv/ko_fans_fos/'
output_file3 = '../data/bigv/ki_fans_fans/'
output_file4 = '../data/bigv/ki_fans_fos/'
'''
output_file1 = '../data/bigv/ko_fans_statuses/'
output_file2 = '../data/bigv/ki_fans_statuses/'
bigv = {}


def load_bigv(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split('\t')
            bigv[row[0]] = [row[2], row[3]]


def slice_bigv():
    KO, KI = defaultdict(list), defaultdict(list)
    for u in bigv:
        id_ko = int(math.log(int(bigv[u][1]), 2))
        id_ki = int(math.log(int(bigv[u][0]), 2))
        KO[id_ko].append(u)
        KI[id_ki].append(u)
    return KO, KI


def stat_fans(KO, KI, path1, path2, path3, path4):
    KO_fans_fans, KO_fans_fos = {}, {}
    KI_fans_fans, KI_fans_fos = {}, {}
    conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
    cur = conn.cursor()
    try:
        for key1 in KO:
            temp1, temp2 = [], []
            for e in KO[key1]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res1 = cur.fetchall()
                for fa in res1[0][0].strip().split('\t'):
                    cur.execute('Select fos, fas from fa_sample_table where id = %s' % fa)
                    res2 = cur.fetchall()
                    temp1.append(res2[0][1])
                    temp2.append(res2[0][0])
            KO_fans_fans[key1] = temp1
            KO_fans_fos[key1] = temp2
        for key2 in KI:
            temp3, temp4 = [], []
            for e in KI[key2]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res3 = cur.fetchall()
                for fa in res3[0][0].strip().split('\t'):
                    cur.execute('Select fos, fas from fa_sample_table where id = %s' % fa)
                    res4 = cur.fetchall()
                    temp3.append(res4[0][1])
                    temp4.append(res4[0][0])
            KI_fans_fans[key2] = temp3
            KI_fans_fos[key2] = temp4
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    for key in KO_fans_fans:
        with open(path1+str(key), 'w') as write_file:
            for e in KO_fans_fans[key]:
                write_file.write('%s\n' % e)
    for key in KO_fans_fos:
        with open(path2+str(key), 'w') as write_file:
            for e in KO_fans_fos[key]:
                write_file.write('%s\n' % e)
    for key in KI_fans_fans:
        with open(path3+str(key), 'w') as write_file:
            for e in KI_fans_fans[key]:
                write_file.write('%s\n' % e)
    for key in KI_fans_fos:
        with open(path4+str(key), 'w') as write_file:
            for e in KI_fans_fos[key]:
                write_file.write('%s\n' % e)


def stat_statuses(KO, KI, path1, path2):
    KO_fans_statuses, KI_fans_statuses = {}, {}
    conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
    cur = conn.cursor()
    try:
        for key1 in KO:
            temp1 = []
            for e in KO[key1]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res1 = cur.fetchall()
                for fa in res1[0][0].strip().split('\t'):
                    cur.execute('Select statuses_count from fa_sample_table where id = %s' % fa)
                    res2 = cur.fetchall()
                    if len(res2) != 0:
                        temp1.append(res2[0][0])
            KO_fans_statuses[key1] = temp1
        for key2 in KI:
            temp2 = []
            for e in KI[key2]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res3 = cur.fetchall()
                for fa in res3[0][0].strip().split('\t'):
                    cur.execute('Select statuses_count from fa_sample_table where id = %s' % fa)
                    res4 = cur.fetchall()
                    if len(res4) != 0:
                        temp2.append(res4[0][0])
            KI_fans_statuses[key2] = temp2
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    for key in KO_fans_statuses:
        with open(path1+str(key), 'w') as write_file:
            for e in KO_fans_statuses[key]:
                write_file.write('%s\n' % e)
    for key in KI_fans_statuses:
        with open(path2+str(key), 'w') as write_file:
            for e in KI_fans_statuses[key]:
                write_file.write('%s\n' % e)


if __name__ == '__main__':
    load_bigv(bigv_path)
    KO, KI = slice_bigv()
    # stat_fans(KO, KI, output_file1, output_file2, output_file3, output_file4)
    stat_statuses(KO, KI, output_file1, output_file2)
