# coding=utf-8

import numpy
import cmath
import random

N_NODE = 100 * 1000
MAX_K = 500
average_k = 50


def pick_degree(sum_p):
    temp_p = random.random()
    for k in range(len(sum_p)):
        if temp_p <= sum_p[k].real:
            return k
    return len(sum_p) - 1


def pick_node(k, n_node, id_itself):
    neib_nodes = set()
    num_picked = 0
    while num_picked < k:
        node_id = random.randint(1, n_node-1)
        if node_id != id_itself and node_id not in neib_nodes:
            neib_nodes.add(node_id)
            num_picked += 1
    return sorted(neib_nodes)


def gen_possion_distribution(c, max):  # 0 to max
    p = [0] * (max + 1)
    sum = [0] * (max + 1)
    p[0] = cmath.exp(-c)
    sum[0] = p[0]
    for i in range(1, max):
        p[i] = p[i - 1] * c / i
        sum[i] = sum[i - 1] + p[i]
    sum[max] = 1.0
    return (p, sum)


def generate_ER(n_node, average_k, max_k, the_network):
    (p_k, cum_pk) = gen_possion_distribution(average_k, max_k)
    num_edges = 0
    for node_id in range(n_node):
        degree = pick_degree(cum_pk)
        num_edges += degree
        neighbors = pick_node(degree, n_node, node_id)
        for node_id_2 in neighbors:
            the_network[node_id].append(node_id_2)


def Gen_ER():
    the_network = [[]] * N_NODE
    for node in range(N_NODE):
        the_network[node] = []
    generate_ER(N_NODE, average_k, MAX_K, the_network)
    out_file = open('D:/Projects/Matlab/SIR_simu/Data/ER_outLinks_10w.txt', 'w')
    for node in range(N_NODE):
        out_file.write('%d\t' % node)
        for item in the_network[node]:
            out_file.write(str(item))
            out_file.write('\t')
        out_file.write('\n')
        # print >> out_file, the_network[node]
    out_file.close()


if __name__ == "__main__":
    Gen_ER()
