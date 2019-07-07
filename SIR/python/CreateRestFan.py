# coding=utf-8
from collections import defaultdict

InputFile1 = 'D:/Projects/Pycharm/SIR/Data/TXT/RestUser_tmp'
InputFile2 = 'F:/Research备份/Data/微博2017@大军/AllFollwers/result'
OutputFile1 = 'D:/Projects/Pycharm/SIR/Data/Dict/RestUser_dict.txt'
OutputFile2 = 'D:/Projects/Pycharm/SIR/Data/TXT/RestUserFan'

Rest_Dict = {}
Rest_Fan_Dict = defaultdict(list)


def saveRestUD(path):
    with open(path, 'w') as OutF:
        for item in Rest_Dict:
            OutF.write(item)
            OutF.write('\t')
            OutF.write(Rest_Dict[item])
            OutF.write('\n')


def saveRestUser(path):
    with open(path, 'w') as OutF:
        for item in Rest_Fan_Dict:
            OutF.write(item)
            OutF.write(':')
            for e in Rest_Fan_Dict[item]:
                OutF.write(e)
                OutF.write('\t')
            OutF.write('\n')


def CreateRestFan(path1, path2):
    with open(path1, 'r') as InF:
        idx = 432908953
        for eachLine in InF:
            idx += 1
            eachLine = eachLine.strip('\n')
            Rest_Dict[eachLine] = str(idx)
    with open(path2, 'r') as InF:
        cnt = 0
        for eachLine in InF:
            cnt += 1
            if cnt % 100000 == 0:
                print(cnt)
            eachLine = eachLine.split(':')
            eachLine = eachLine[2].split('[')
            eachLine = eachLine[1]
            eachLine = eachLine.split(']')
            eachLine = eachLine[0]
            eachLine = eachLine.split(',')
            for item in eachLine:
                if item in Rest_Dict:
                    Rest_Fan_Dict[Rest_Dict[item]].append(str(cnt))


def stat(path1, path2):
    dict1 = defaultdict(list)
    dict2 = {}
    with open(path1, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip('\n')
            eachLine = eachLine.split('\t')
            dict1[eachLine[1]].append(eachLine[0])
    with open(path2, 'r') as InF:
        for eachLine in InF:
            eachLine = eachLine.strip()
            eachLine = eachLine.split(':')
            s = eachLine[1]
            s = s.split('\t')
            dict2[eachLine[0]] = len(s)
    for elem in dict1:
        if elem in dict2:
            dict1[elem].append(dict2[elem])

    with open('D:/Projects/Pycharm/SIR/Data/TXT/RestUser', 'w') as OutF:
        for elem in dict2:
            OutF.write(elem)
            OutF.write('\t')
            OutF.write(dict1[elem][0])
            OutF.write('\t')
            OutF.write(str(dict1[elem][1]))
            OutF.write('\n')


if __name__ == '__main__':
    # CreateRestFan(InputFile1, InputFile2)
    # saveRestUD(OutputFile1)
    # saveRestUser(OutputFile2)
    stat(OutputFile1, OutputFile2)
