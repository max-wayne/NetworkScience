# coding = utf-8

import MySQLdb

InputFile = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'


def createUserDictDB(path):

    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    cnt = 0
    try:
        cur.execute("DROP TABLE IF EXISTS User_TABLE")
        cur.execute("create table User_Table(id int primary key, uid longtext) engine=myisam")
        with open(path, 'r') as InF:
            for eachLine in InF:
                cnt += 1
                if cnt % 100000 == 0:
                    print(cnt)
                eachLine = eachLine.split('\t')
                uid = eachLine[0]
                id = eachLine[1]
                record = (int(id), str(uid))
                cur.execute('INSERT INTO User_Table values(%s,%s)', record)
    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    createUserDictDB(InputFile)
