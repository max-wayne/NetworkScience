# coding=utf-8
# Just add the original table
import MySQLdb

InputFile1 = 'D:/Projects/Pycharm/SIR/Data/TXT/RestUser'
InputFile2 = 'D:/Projects/Pycharm/SIR/Data/TXT/RestUserFan'


def CreateRestDB(path1, path2):

    conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='admin#_#', db='weibodata')
    cur = conn.cursor()

    try:
        with open(path1, 'r') as InF:
            cnt1 = 0
            for eachLine in InF:
                cnt1 += 1
                print(cnt1)
                eachLine = eachLine.strip('\n')
                eachLine = eachLine.split('\t')
                cur.execute('Insert into user_table(id, uid, fas) values(%s, %s, %s)', (eachLine[0], eachLine[1], eachLine[2]))

        with open(path2, 'r') as InF:
            cnt2 = 0
            for eachLine in InF:
                cnt2 += 1
                print(cnt2)
                eachLine = eachLine.strip()
                eachLine = eachLine.split(':')
                cur.execute('Insert into fa_table values(%s, %s)', (eachLine[0], eachLine[1]))

    except:
        import traceback
        traceback.print_exc()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    CreateRestDB(InputFile1, InputFile2)
