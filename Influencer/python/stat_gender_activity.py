# coding=utf-8
import pymysql

bigv_path = '../data/influencer'

bigv = {}
gender = {}


def load_bigv(path):
    with open(path, 'r') as read_file:
        for row in read_file:
            row = row.strip('\n').split('\t')
            bigv[row[0]] = [row[2], row[3]]


def stat_gender():
    conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
    cur = conn.cursor()
    try:
        for u in bigv:
            m, f = 0, 0
            cur.execute('Select fa_sample from bigv_table where id = %s' % u)
            res1 = cur.fetchall()
            for fa in res1[0][0].strip().split('\t'):
                cur.execute('Select gender from fa_sample_table where id = %s' % fa)
                res2 = cur.fetchall()
                if len(res2) != 0:
                    if res2[0][0] == 'm':
                        m += 1
                    else:
                        f += 1
            gender[u] = [m/(m+f), f/(m+f)]
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    with open('../data/bigv/gender', 'w') as write_file:
        for u in gender:
            write_file.write('%s\t%s\t%s\t%s\t%s\n' % (u, bigv[u][0], bigv[u][1], gender[u][0], gender[u][1]))


if __name__ == '__main__':
    load_bigv(bigv_path)
    stat_gender()
