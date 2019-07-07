# coding=utf-8

input_file = 'D:/Projects/Pycharm/SIR/Data/45/file'
output_file = 'D:/Projects/Pycharm/SIR/Data/45/all_retweet_user'
FILE = []
all_retweet_user = set()


def read_file(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.strip('\n')
            FILE.append(row)


def assemble(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.split('\t')
            for item in row[0: 2]:
                if item not in all_retweet_user:
                    all_retweet_user.add(item)


def write_file(path):
    with open(path, 'w') as write_handle:
        for item in all_retweet_user:
            write_handle.write('%s\n' % item)


if __name__ == '__main__':
    read_file(input_file)
    cnt = 0
    for file in FILE:
        cnt += 1
        print(cnt)
        s = 'D:/Projects/Pycharm/SIR/Data/55/' + file + '/FinalTrace'
        assemble(s)
    write_file(output_file)