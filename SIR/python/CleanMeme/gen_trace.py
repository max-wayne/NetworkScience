# coding=utf-8
import pymysql
import time
from operator import itemgetter


def gen_trace(path1, path2):
    mid_uid_dict = {}
    trace = []
    with open(path1, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n').split('\t')
            mid_uid_dict[row[3]] = row[2]
    with open(path1, 'r') as read_f:
        for row in read_f:
            row = row.strip('\n').split('\t')
            s = (row[5].strip()).split(' +0800')
            t = time.strptime(s[0] + s[1])
            if row[4].strip() == row[0]:
                trace.append([row[2], row[1], row[5], str(time.mktime(t))])
            else:
                if row[4].strip() in mid_uid_dict:
                    trace.append([row[2], mid_uid_dict[row[4].strip()], row[5], str(time.mktime(t))])
                else:
                    continue
    # 生成按时间先后的转发轨迹
    new_trace = []
    conn = pymysql.connect('localhost', 'root', 'admin#_#', 'weibodata')
    cur = conn.cursor()
    try:
        for item in trace:
            u1, u2 = item[0], item[1]
            cur.execute('Select id,fos from user_table where uid = %s' % u1)
            res1 = cur.fetchall()
            if len(res1) != 0:  # 保证用户在这4亿里面
                cur.execute('Select id,fos from user_table where uid = %s' % u2)
                res2 = cur.fetchall()
                if len(res2) != 0:
                    cur.execute('Select fas from temp where id = %s' % res1[0][0])
                    res11 = cur.fetchall()
                    if len(res11) != 0:
                        cur.execute('Select fas from temp where id = %s' % res2[0][0])
                        res22 = cur.fetchall()
                        if len(res22) != 0:
                            new_trace.append((res1[0][0], res2[0][0], item[2], item[3], res1[0][1], res11[0][0],
                                              res2[0][1], res22[0][0]))
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    with open(path2, 'w') as write_f:
        final_trace = sorted(new_trace, key=itemgetter(3))
        for item in final_trace:
            write_f.write('%s\n' % '\t'.join(item))


if __name__ == '__main__':
    input_file = 'meme_name'
    output_file = 'meme_name' + '/FinalTrace'
    gen_trace(input_file, output_file)


