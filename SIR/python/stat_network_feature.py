# coding=utf-8

user_k_path = 'D:/Projects/Pycharm/SIR/data/info_stat/UserK'

user_k_c = {}
N = 432908953


def stat_network_feature(path):
    k_first_order, k_second_order, m, n = 0, 0, 0, 0
    with open(path, 'r') as read_f:
        cnt = 0
        for row in read_f:
            cnt += 1
            if cnt % 10000000 == 0:
                print(cnt/10000000)
            row = row.strip('\n').split('\t')
            ki = int(row[1])
            ko = int(row[2]) if len(row) == 3 else 0
            m += ki
            n += ko
            k_first_order += ki + ko
            k_second_order += ki * ko
            if (ki, ko) not in user_k_c:
                user_k_c[(ki, ko)] = 1
            else:
                user_k_c[(ki, ko)] += 1
    with open('D:/Projects/Pycharm/SIR/data/info_stat/KI-KO-N', 'w') as write_f:
        for key in user_k_c:
            write_f.write('%s\t%s\t%s\n' % (key[0], key[1], str(user_k_c[key])))
    with open('D:/Projects/Pycharm/SIR/data/info_stat/network_feature', 'w') as write_f:
        write_f.write('N=%s\n' % str(N))
        write_f.write('M=%s\n' % str(m))
        write_f.write('Ki_avg=%s\n' % str(m/N))
        write_f.write('Ko_avg=%s\n' % str(n/N))
        write_f.write('K_Avg=%s\n' % str(k_first_order/(2*N)))
        write_f.write('K_Cor=%s\n' % str(k_second_order/N))
        write_f.write('beta_c=%s\n' % str(k_first_order/k_second_order/2))


if __name__ == '__main__':
    stat_network_feature(user_k_path)


