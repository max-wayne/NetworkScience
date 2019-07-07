# coding=utf-8

InputFile = 'D:/Search/Data/Weibo/AllFollow/result'
OutputFile = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'

startStr = '{"uid":'
endStr = ',"'


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


# 将离散化后的user_id以TXT形式保存
def GetUserDict(path1, path2):
    idx = 1
    with open(path2, 'w') as OuF:
        with open(path1, 'r') as InF:
            for eachLine in InF:
                if idx % 100000 == 0:
                    print(idx)
                key = GetMiddleStr(eachLine, startStr, endStr)
                OuF.write(key)
                OuF.write('\t')
                OuF.write(str(idx))
                OuF.write('\n')
                idx += 1


if __name__ == '__main__':
    GetUserDict(InputFile, OutputFile)
