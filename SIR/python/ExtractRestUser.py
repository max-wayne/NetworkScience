# coding=utf-8
import MySQLdb

InputFile1 = 'D:/Projects/Pycharm/SIR/Data/Big_Info/2017/FILENAME'
InputFile2 = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'
OutputFile = 'D:/Projects/Pycharm/SIR/Data/TXT/RestUser_tmp'
FILENAME = []
User_D = set()
REST = set()


def loadF(path):
    with open(path, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip('\n')
            FILENAME.append(eachLine)


def loadD(path):
    with open(path, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip('\n')
            eachLine = eachLine.split('\t')
            User_D.add(eachLine[0])


def Extract(path):
    with open(path, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip()
            eachLine = eachLine.split('\t')
            for uid in eachLine[0:2]:
                if uid not in User_D:
                    REST.add(uid)


def saveRest(path):
    with open(path, 'w') as OutF:
        for item in REST:
            OutF.write(item)
            OutF.write('\n')


if __name__ == '__main__':
    loadF(InputFile1)
    loadD(InputFile2)
    cnt = 0
    for file in FILENAME:
        cnt += 1
        print(cnt)
        path = 'D:/Projects/Pycharm/SIR/Data/Big_Info/2017/' + file + '/trace'
        Extract(path)
    print(len(REST))
    saveRest(OutputFile)
