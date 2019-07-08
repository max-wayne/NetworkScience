# coding=utf-8

import pymysql
import time
import re

bigv_path = '../data/bigv_20/bigv_20.txt'
influencer_path = '../data/influencer'
BIGV = []
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
start_time = time.mktime(time.strptime('2018-07-01', '%Y-%m-%d'))


def load_bigv(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split('\t')
            BIGV.append(row[0])


def extract_fans():
    try:
        conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata', use_unicode=True, charset="utf8")
        cur = conn.cursor()
        cnt = 0
        for user in BIGV:
            cnt += 1
            if cnt % 100 == 0:
                print(cnt)
            output = '../data/bigv/bigv_fans/' + user
            fans_dict = {}
            cur.execute('Select fa_sample from bigv_table where id = %s' % user)
            res1 = cur.fetchall()
            for fan in res1[0][0].split('\t')[:-1]:
                cur.execute('Select * from fa_sample_table where id = %s' % fan)
                res2 = cur.fetchall()
                fans_dict[fan] = res2[0]
            with open(output, 'w', encoding='utf-8') as write_file:
                for key in fans_dict:
                    s = []
                    for item in fans_dict[key]:
                        s.append(str(item))
                    write_file.write('\t'.join(s))
                    write_file.write('\n')
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


def stat_activity(path):
    with open(path, 'r', encoding='utf-8') as read_file:
        cnt1, cnt2 = 0, 0
        for row in read_file:
            cnt1 += 1
            row = row.strip('\n').split('\t')
            if row[2] != 'none':
                flag = zh_pattern.search(row[2])
                if flag or len(row[2]) == 5:
                    cnt2 += 1
                elif len(row[2]) == 10:
                    t = time.mktime(time.strptime(row[2], '%Y-%m-%d'))
                    if start_time <= t:
                        cnt2 += 1
        activity = cnt2 / cnt1
        return activity


if __name__ == '__main__':
    load_bigv(influencer_path)
    # extract_fans()
    A_dict = {}
    for u in BIGV:
        u_path = '../data/bigv/bigv_fans/' + u
        a = stat_activity(u_path)
        A_dict[u] = a
    with open('../data/bigv/2018_07_01', 'w') as write_file:
        for key in A_dict:
            write_file.write('%s\t%s\n' % (key, A_dict[key]))



