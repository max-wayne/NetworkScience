# coding = uft-8
import MySQLdb
import datetime

InputFile = 'D:/Projects/Pycharm/SIR/Data/TXT/Fa_TXT'


def CreateFan_DB(path):
    # 创建数据库
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS Fa_Table")
        cur.execute("Create table Fa_Table(id int primary key, fa longtext) engine=myisam")
        with open(path, 'r') as InF:
            cnt = 0
            for eachLine in InF:
                cnt += 1
                eachLine = eachLine.strip()
                info = eachLine.split(':')
                cur.execute('INSERT INTO Fa_Table values(%s, %s)', (info[0], info[1]))
    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    StartTime = datetime.datetime.now()
    CreateFan_DB(InputFile)
    EndTime = datetime.datetime.now()
    print(EndTime - StartTime)
