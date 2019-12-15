# -*- coding: utf-8 -*-
import argparse
import pickle as pk
import sys

parent = {}  # key: node, value: the highest parent node
rank = {}  # key: node,  value: rank of each node

def make_set(v):
    parent[v] = v
    rank[v] = 0

def make_edges(graph):
    # input: list of list
    # output: dictionary
    edges = []
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            edges.append((graph[i][j], str(i), str(j)))
            edges.append((graph[j][i], str(j), str(i)))
    return edges

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

# graph is a list in list and graph[i][j] means a cost to go city i to city j
def kruskal(graph):
    mst = []
    edges = make_edges(graph)
    edges.sort()

    for i in range(len(graph)):
        make_set(str(i))

    for edge in edges:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return mst

# this function is not used now
def make_graph(edges, num):
    # num: 전체 edge의 수
    # input: list [(weight(int), 'city'(char), 'city'(char) ... ]
    # output: list of list
    # [(1, '0', '1'), (2, '1', '2')]
    graph = [[0 for col in range(num)] for row in range(num)]
    for edge in edges:
        weight, v, u = edge
        pass

def development(cities, roads, airports):
    roads_list = []
    airports_list = []
    # your codes goes here
    T = kruskal()

    return roads_list, airports_list

'''
planTransit(costs c_{i, j}, a_i):
    generate the graph G as above
    T = KRUSKAL(G)
    T_sky = KRUSKAL( G_sky )
    if cost(T) < cost(T_sky):
        T_actual = T
    else
        T_actual = T_sky
    airports = []
    roads = []
    for i in range(1, n):
        if {v_i, air} is an edge in T_actual:
            airports.add(i)
        for j in range(1, n):
            if {v_i, v_j} is an edge in T_actual:
                roads.add( {i, j} )
    return airports, roads
'''

'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cities", type=int, default=10, help="the number of cities")
    parser.add_argument("--roads", type=str, default="./roads.pk", help="road information")
    parser.add_argument("--airports",type =str, default = './airports.pk', help ="airports information")
    opt = parser.parse_args()

    cities = opt.cities

    f1 = open(opt.roads,"rb")
    f2 = open(opt.airports,"rb")

    roads = pk.load(f1)
    airports = pk.load(f2)

    f1.close()
    f2.close()

    road_list, airport_list = development(cities, roads, airports)

    print("Roads : ", end = "")
    print(road_list)

    print("Airports : ", end = "")
    print(airport_list)
    '''