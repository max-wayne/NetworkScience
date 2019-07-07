# coding = uft-8
import MySQLdb

Follower_Dict = []
path = 'D:/Projects/Pycharm/SIR/Data/TXT/Fo_TXT'

def GetMiddleStr(content, startStr, endStr):
    try:
        startIndex = content.index(startStr)
    except:
        return []
    if startIndex >= 0:
        startIndex += len(startStr)
    try:
        endIndex = content.index(endStr)
    except:
        return []
    return content[startIndex:endIndex]


def CreateFo_DB(path):
    # 创建数据库
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE IF EXISTS Fo_TABLE")
        cur.execute("create table Fo_Table(id int primary key, fo longtext) engine=myisam")
        with open(path, 'r') as InF:
            cnt = 0
            for eachLine in InF:
                cnt += 1
                if cnt % 100000 == 0:
                    print(cnt)
                eachLine = eachLine.strip()
                info = eachLine.split(':')
                record = (int(info[0]), str(info[1]))
                cur.execute('INSERT INTO Fo_Table values(%s, %s)', record)
    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    CreateFo_DB(path)
