# coding=utf-8
from collections import defaultdict

input_file1 = 'D:/Projects/Pycharm/SIR/Data/info_stat/RepostCountReal.txt'
input_file2 = 'D:/Projects/Pycharm/SIR/Data/info_stat/SpreadTree.txt'
output_file = 'D:/Projects/Pycharm/SIR/Data/info/big_info/'

mid = []
ratio = 0.9
repost_dict = defaultdict(list)


def extract_big_info(path1, path2, path3):
    with open(path1, 'r', encoding='utf-8') as read_f:
        for row in read_f:
            row = row.split('\t')
            if int(row[1]) != 0:
                res = int(row[2])/int(row[1])
                if res >= ratio:
                    mid.append(row[0])
    with open(path2, 'r', encoding='utf-8') as read_f:
        cnt = 0
        for row in read_f:
            cnt += 1
            if cnt % 10000 == 0:
                print(cnt)
            row = row.split("'")
            if row[1] in mid:
                record = row[3]+'\t'+row[5]+'\t'+row[7]+'\t'+row[9]+'\t'+row[11]
                repost_dict[row[1]].append(record)
    for key in repost_dict:
        s = path3 + str(key)
        with open(s, 'w') as write_f:
            write_f.write('%s\t%s\n' % (key, '\t'.join(repost_dict[key])))


if __name__ == '__main__':
    extract_big_info(input_file1, input_file2, output_file)
