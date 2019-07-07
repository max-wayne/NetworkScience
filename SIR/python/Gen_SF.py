# coding=utf-8
import random

N_NODE = 100000
MAX_K = 1000
MIN_K = 2


def pick_degree(cum_pk):
    temp_p = random.random()
    for k in range(len(cum_pk)):
        if temp_p <= cum_pk[k].real:
            return k
    return len(cum_pk)-1


def pick_node(k, n_node, id_itself):
    neib_nodes = set()
    num_picked = 0
    while num_picked < k:
        node_id = random.randint(1, n_node-1)
        if node_id != id_itself and node_id not in neib_nodes:
            neib_nodes.add(node_id)
            num_picked += 1
    return sorted(neib_nodes)


def gen_cum_powerlaw_distribution(min_k, max_k, gamma):
    pk_f = [0.0] * (max_k + 1)
    sum = 0.0
    for k in range(min_k, max_k + 1):
        temp = pow(k, -gamma)
        pk_f[k] = temp
        sum += temp
    for k in range(min_k, max_k + 1):
        pk_f[k] = pk_f[k] / sum + pk_f[k-1]
    pk_f[max_k] = 1.0
    return pk_f


def generate_SF(n_node, max_k, min_k, the_network):
    gamma = 2.5
    cum_pk = gen_cum_powerlaw_distribution(min_k, max_k, gamma)
    num_edges = 0
    for node_id in range(n_node):
        degree = pick_degree(cum_pk)
        num_edges += degree
        neighbors = pick_node(degree, n_node, node_id)
        for node_id_2 in neighbors:
            the_network[node_id].append(node_id_2)


def Gen_SF():
    the_network = [[]] * N_NODE
    for node in range(N_NODE):
        the_network[node] = []
    generate_SF(N_NODE, MAX_K, MIN_K, the_network)
    with open('D:/Projects/Pycharm/SIR_Simu/Data/Net/SF_outlinks_10w_hyw.txt', 'w') as OutF:
        for node in range(N_NODE):
            OutF.write(str(node))
            OutF.write('\t')
            for item in the_network[node]:
                OutF.write(str(item))
                OutF.write('\t')
            OutF.write('\n')


if __name__ == '__main__':
    Gen_SF()
