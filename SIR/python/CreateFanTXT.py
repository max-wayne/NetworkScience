# coding = utf-8
import datetime
from collections import defaultdict

InputFile = 'E:/weibo/TXT/Fo_TXT'
OutputFile = 'D:/Projects/Pycharm/SIR/Data/TXT/Fa_TXT_final'   # format: (id : fan1 fan2 ...)

Fan_Dict = defaultdict(list)


def CreateFan_TXT(path1, path2):

    start = 0
    end = 10000000

    with open(path2, 'w') as OutF:
        # 生成字典
        Fan_Dict.clear()
        with open(path1, 'r') as InF:
            for eachLine in InF:
                results = eachLine.split(':')
                if len(results[1]) != 1:
                    results[1] = results[1].strip()
                    for item in results[1].split('\t'):
                        if start < int(item) <= end:
                            Fan_Dict[item].append(results[0])
        # 将字典写入TXT
        for elem in Fan_Dict:
            OutF.write(str(elem))
            OutF.write(':')
            for e in Fan_Dict[elem]:
                OutF.write(str(e))
                OutF.write('\t')
            OutF.write('\n')


if __name__ == '__main__':
    Start = datetime.datetime.now()
    CreateFan_TXT(InputFile, OutputFile)
    End = datetime.datetime.now()
    print(End-Start)


