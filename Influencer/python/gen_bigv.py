# coding=utf-8

user_k = 'D:/Projects/Pycharm/SIR/Data/Info_stat/UserK'
influencer_id = '../data/influencer'


def find_influencer(path1, path2):
    user = []
    with open(path1, 'r') as read_f:
        cnt = 0
        for row in read_f:
            cnt += 1
            if cnt % 1000000 == 0:
                print(cnt)
            row = row.strip('\n')
            row = row.split('\t')
            if len(row) == 3 and int(row[2]) > 500000:
                user.append(row[0]+'\t'+row[1]+'\t'+row[2]+'\n')
    with open(path2, 'w') as write_f:
        for item in user:
            write_f.write(item)


if __name__ == '__main__':
    find_influencer(user_k, influencer_id)
