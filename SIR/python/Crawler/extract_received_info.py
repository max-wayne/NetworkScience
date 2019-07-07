# coding=utf-8

input_file = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user'
output_file1 = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user_info_temp1'
output_file2 = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user_info_temp2'
output_file3 = 'D:/Projects/Pycharm/SIR/Data/45/all_received_user_info'

User_Dict_path = 'D:/Projects/Pycharm/SIR/Data/Dict/User_Dict.txt'
UserK_path = 'D:/Projects/Pycharm/SIR/Data/Info_stat/UserK'
user = set()
User_Dict = {}
User_K = {}


def read_user(path):
    with open(path, 'r') as read_handle:
        cnt = 0
        for row in read_handle:
            cnt += 1
            if cnt in range(180000000, 186879928):
                row = row.strip('\n')
                user.add(row)
    print('reading user done...')


def load_dict(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.strip('\n')
            row = row.split('\t')
            User_Dict[row[1]] = row[0]
    print('loading user_dict done...')


def write_file_uid(path):
    with open(path, 'w') as write_handle:
        for u in user:
            write_handle.write('%s\t%s\n' % (u, User_Dict[u]))
    print('writing uid done...')


def load_userk(path):
    with open(path, 'r') as read_handle:
        for row in read_handle:
            row = row.strip('\n')
            row = row.split('\t')
            if len(row) == 3:
                User_K[row[0]] = row[1] + '\t' + row[2]
            else:
                User_K[row[0]] = row[1]
    print('loading userk done...')


def write_file_k(path):
    with open(path, 'w') as write_handle:
        for u in user:
            write_handle.write('%s\t%s\n' % (u, User_K[u]))
    print('writing userk done...')


def assemble(path1, path2, path3):
    dict1 = {}
    dict2 = {}

    with open(path1, 'r') as read_handle1:
        for row in read_handle1:
            row = row.strip('\n')
            row = row.split('\t')
            dict1[row[0]] = row[1]
    with open(path2, 'r') as read_handle2:
        for row in read_handle2:
            row = row.strip('\n')
            row = row.split('\t')
            if len(row) == 3:
                dict2[row[0]] = row[1] + '\t' + row[2]
            else:
                dict2[row[0]] = row[1]
    with open(path3, 'a') as write_handle:
        for key in dict1:
            write_handle.write('%s\t%s\t%s\n' % (key, dict1[key], dict2[key]))
    print('assemble done!')


if __name__ == '__main__':
    read_user(input_file)
    load_dict(User_Dict_path)
    write_file_uid(output_file1)
    User_Dict.clear()
    load_userk(UserK_path)
    write_file_k(output_file2)
    User_K.clear()
    assemble(output_file1, output_file2, output_file3)