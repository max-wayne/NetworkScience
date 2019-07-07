# coding = uft-8

InputFile1 = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'
InputFile = 'D:/Search/Data/Weibo/AllFollow/result'
OutputFile = 'D:/Projects/Pycharm/SIR/Data/TXT/Fo_TXT'  # format: (id : follower1 follower2 ...)

s1 = '{"uid":'
s2 = ',"ids":['
s3 = ']}'

User_Dict = {}


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


def Load_UserDict(path):
    # 读入离散化用户字典
    with open(path, 'r') as InF:
        cnt = 1
        for eachLine in InF:
            if cnt % 100000 == 0:
                print('cnt_dict=', cnt)
            eachLine = eachLine.split('\t')
            User_Dict[eachLine[0]] = int(eachLine[1])
            cnt += 1


def CreateFo_TXT(path1, path2):

    cnt = 0
    f = open(path2, 'w')
    with open(path1, 'r') as InF:
        for eachLine in InF:
            cnt += 1
            if cnt % 100000 == 0:
                print('cnt_InF=', cnt)
            uid = GetMiddleStr(eachLine, s1, s2)
            f.write(str(User_Dict.get(uid)))
            f.write(':')
            for item in GetMiddleStr(eachLine, s2, s3).split(','):
                if User_Dict.get(item, 0) != 0:     #丢弃不在网络中的节点
                    f.write(str(User_Dict.get(item, 0)))
                    f.write('\t')
            f.write('\n')
    f.close()


if __name__ == "__main__":
    Load_UserDict(InputFile1)
    CreateFo_TXT(InputFile, OutputFile)
