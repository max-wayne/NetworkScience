# coding=utf-8
from collections import defaultdict

User_Dict = {}
InputFile1 = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'
InputFile2 = 'F:/Research备份/Data/微博2017@大军/AllFollwers/result'
OutputFile1 = 'D:/Projects/Pycharm/SIR/Data/Dict/Add_User_Dict'
OutputFile2 = 'D:/Projects/Pycharm/SIR/Data/TXT/New_User_Fans'

start = 15000000
interval = 5000000
cnt = 493134901


def loadUD(path):
    with open(path, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip('\n')
            eachLine = eachLine.split('\t')
            User_Dict[eachLine[0]] = eachLine[1]


def Extract_RestUser(path, cnt, start, end, path1, path2):
    Add_User_Dict = {}
    Fans_Dict = defaultdict(list)
    with open(path, 'r') as InF:
        num = 0
        for eachLine in InF:
            num += 1
            if num % 100000 == 0:
                print(num)
            if (num <= end) and (num >= start):
                eachLine = eachLine.split(':')
                uid = eachLine[1].split(',')[0]
                eachLine = eachLine[2].split('[')
                eachLine = eachLine[1]
                eachLine = eachLine.split(']')
                eachLine = eachLine[0]
                eachLine = eachLine.split(',')
                for item in eachLine:
                    if item not in User_Dict:
                        if item not in Add_User_Dict:
                            cnt += 1
                            Add_User_Dict[item] = str(cnt)
                            Fans_Dict[str(cnt)].append(User_Dict[uid])
                        else:
                            Fans_Dict[Add_User_Dict[item]].append(User_Dict[uid])
            elif num == end + 1:
                break
    print('cnt=', cnt)

    with open(path1, 'w') as OutF:
        for item in Add_User_Dict:
            OutF.write(item)
            OutF.write('\t')
            OutF.write(Add_User_Dict[item])
            OutF.write('\n')

    with open(path2, 'w') as OutF:
        for item in Fans_Dict:
            OutF.write(item)
            OutF.write(':')
            for e in Fans_Dict[item]:
                OutF.write(e)
                OutF.write('\t')
            OutF.write('\n')

    return cnt


if __name__ == '__main__':
    loadUD(InputFile1)
    for i in range(4, 86):
        print('i=', i)
        end = start + interval
        path1 = OutputFile1 + str(i)
        path2 = OutputFile2 + str(i)
        idx = Extract_RestUser(InputFile2, cnt, start, end, path1, path2)
        start = end
        cnt = idx
