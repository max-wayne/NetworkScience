# coding=utf-8
import MySQLdb
import datetime
MAX = 100000000


def CountNum():

    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    try:
        for i in range(MAX+1):
            if i % 100000 == 0:
                print(i)
            cur.execute('Select fa from fa_table where id=%s' % str(i))
            results = cur.fetchall()
            if len(results) != 0:
                fans = results[0][0].strip()
                num = len(fans.split('\t'))
                cur.execute('Update user_table set fas=%s WHERE id = %s', (str(num), str(i)))
        conn.autocommit('on')
    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    startTime = datetime.datetime.now()
    CountNum()
    endTime = datetime.datetime.now()
    print(endTime-startTime)
