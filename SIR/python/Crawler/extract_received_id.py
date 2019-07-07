# coding=utf-8
import MySQLdb

input_file = 'D:/Projects/Pycharm/SIR/Data/45/all_retweet_user'
output_file = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user'
user = set()
fan = set()


def read_user(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.strip('\n')
            user.add(row)


def query():
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    try:
        cnt = 0
        for item in user:
            cnt += 1
            if cnt % 1000 == 0:
                print(cnt)
            cur.execute('Select fa from fa_table where id = %s' % item)
            res = cur.fetchall()
            for e in res[0][0].split('\t'):
                if e not in fan:
                    fan.add(e)
    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


def write_file(path):
    with open(path, 'w') as write_handle:
        for item in fan:
            write_handle.write('%s\n' % item)


if __name__ == '__main__':
    read_user(input_file)
    query()
    write_file(output_file)