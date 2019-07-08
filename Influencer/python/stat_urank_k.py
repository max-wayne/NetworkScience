# coding=utf-8
import math
import pymysql
from collections import defaultdict

bigv_path = '../data/influencer'
output_file1 = '../data/bigv/ko_urank/'
output_file2 = '../data/bigv/ki_urank/'
bigv = {}


def load_bigv(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split('\t')
            bigv[row[0]] = [row[2], row[3]]


def slice_bigv(path1, path2):
    KO, KI = defaultdict(list), defaultdict(list)
    for u in bigv:
        id_ko = int(math.log(int(bigv[u][1]), 2))
        id_ki = int(math.log(int(bigv[u][0]), 2))
        KO[id_ko].append(u)
        KI[id_ki].append(u)
    '''
    with open(path1, 'w') as write_file:
        for key in KO:
            write_file.write(str(key))
            write_file.write(':')
            for e in KO[key]:
                write_file.write(e)
                write_file.write('\t')
            write_file.write('\n')
    with open(path2, 'w') as write_file:
        for key in KI:
            write_file.write(str(key))
            write_file.write(':')
            for e in KI[key]:
                write_file.write(e)
                write_file.write('\t')
            write_file.write('\n')
    '''
    return KO, KI


def stat_urank(KO, KI, path1, path2):
    KO_rank = {}
    KI_rank = {}
    conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
    cur = conn.cursor()
    try:
        for key in KO:
            temp = []
            for e in KO[key]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res1 = cur.fetchall()
                for fa in res1[0][0].strip().split('\t'):
                    cur.execute('Select urank from fa_sample_table where id = %s' % fa)
                    res2 = cur.fetchall()
                    if res2[0][0] != 'None':
                        temp.append(res2[0][0])
            KO_rank[key] = temp
        for key in KI:
            temp = []
            for e in KI[key]:
                cur.execute('Select fa_sample from bigv_table where id = %s' % e)
                res1 = cur.fetchall()
                for fa in res1[0][0].strip().split('\t'):
                    cur.execute('Select urank from fa_sample_table where id = %s' % fa)
                    res2 = cur.fetchall()
                    if res2[0][0] != 'None':
                        temp.append(res2[0][0])
            KI_rank[key] = temp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    for key in KO_rank:
        with open(path1+str(key), 'w') as write_file:
            for item in KO_rank[key]:
                if item != 'None':
                    write_file.write(str(item))
                    write_file.write('\n')
    for key in KI_rank:
        with open(path2+str(key), 'w') as write_file:
            for item in KI_rank[key]:
                if item != 'None':
                    write_file.write(str(item))
                    write_file.write('\n')


if __name__ == '__main__':
    load_bigv(bigv_path)
    KO, KI = slice_bigv(output_file1, output_file2)
    stat_urank(KO, KI, output_file1, output_file2)
