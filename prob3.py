# -*- coding: utf-8 -*-
import argparse
import pickle as pk
import sys

parent = {}  # key: node, value: the highest parent node
rank = {}  # key: node,  value: rank of each node

def make_set(v): # 각각의 노드를 전부 분리된 집합으로 만든다
    parent[v] = v # 해당 노드의 부모 노드는 v이다
    rank[v] = 0 # 해당 노드의 랭크는 0이다

def make_edges(graph): # list of list 꼴의 2D 어레이가 들어왔을 때, 이를 (weight, 'city', 'city')로 변환한다.
    # input: list of list
    # output: dictionary
    edges = []
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            edges.append((graph[i][j], str(i), str(j)))
            edges.append((graph[j][i], str(j), str(i)))
    return edges

def find(v): # 해당 노드의 최상위 부모노드를 찾는다
    if parent[v] != v: # 부모 노드가 자기 자신이 나올 때까지 재귀적으로 반복한다.
        parent[v] = find(parent[v])
    return parent[v] # 부모 노드를 리턴한다.

def union(v, u): # 노드 v와 노드 u를 합친다.
    root1 = find(v) # v노드의 최상위 부모노드
    root2 = find(u) # u노드의 최상위 부모노드

    if root1 != root2: # v와 u노드의 최상위 부모노드가 같지 않으면, 즉 이어져있지 않으면
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만든다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1 # root2의 부모노드가 root1이 된다.
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]: #만약 두 노드의 랭크가 같으면
                rank[root2] += 1 # root2 의 자식에 root1을 추가하고  rank를 1 올린다.

def make_graph(edges, num): # [( weight, city1, city2), (weight_b, city1, city3) ... ] 타입의 리스트를 2D array 그래프로 변환하는 함수이다
    # num: 전체 edge의 수
    # input: list [(weight(int), 'city'(char), 'city'(char) ... ]
    # output: list of list
    # [(5, '1', '4'), (5, '3', '5'), (6, '4', '6'), (7, '1', '2'), (7, '2', '5'), (9, '5', '7')]
    graph = [[0 for col in range(num)] for row in range(num)]
    for edge in edges:
        weight, v, u = edge
        graph[int(v)][int(u)] = weight
        graph[int(u)][int(v)] = weight
    return graph

# graph is a list in list and graph[i][j] means a cost to go city i to city j
def kruskal(graph):
    mst = []
    edges = make_edges(graph) # 2D 어레이 형식을 [( weight, city1, city2), (weight_b, city1, city3) ... ] 로 바꾼다.
    edges.sort() # weight의 크기에 따라 정렬한다.

    for i in range(len(graph)):
        make_set(str(i)) #모든 노드를 별개의 집합으로 만든다

    for edge in edges: # 각각의 엣지에 대해
        weight, v, u = edge

        if find(v) != find(u): # u와 v노드가 이어져있지 않으면
            union(v, u) # 이를 잇는다
            mst.append(edge) # 그리고 mst 리스트에 추가한다.

    result = make_graph(mst, len(graph))
    #해당 mst 리스트 형식- [( weight, city1, city2), (weight_b, city1, city3) ... ] - 을 다시 list of list로 바꾼다.
    return result

test = [[0, 2, 4, 11], [2, 0, 7, 9], [4, 7, 0, 6], [11, 9, 6, 0]]
test2 = [12, 9, 1, 3]

# print(make_edges(kruskal(test)))

def development(cities, roads, airports):
    roads_list = []
    airports_list = []
    # your codes goes here
    graph_total = [[0 for col in range(cities)] for row in range(cities+1)] # airport 도시를 추가한 그래프를 생성한다
    for i in range(cities):
        for j in range(i+1, cities):
            graph_total[i][j] = roads[i][j] # airport 도시를 추가한 그래프는 도시끼리는 모두 roads와 동일하다
            graph_total[j][i] = roads[j][i]

    for i in range(cities): # 마지막 도시는 airports이며, 해당 도시에서 airports로 가는 코스트를 추가한다.
        graph_total[i].append(airports[i])
        graph_total[-1][i]=airports[i]
    graph_total[-1].append(0) # airport -> airport 의 코스트는 0이다.

    print(graph_total) # 전체 그래프를 만든 후
    k = kruskal(graph_total) # 크러스컬 알고리즘을 실행하고
    edges = make_edges(k) # 이를 다시 엣지로 분리한다
    print(k)
    airports_name = str(cities+1)

    for edge in edges:
        weight, v, u = edge # 각각의 모든 엣지들에 대해
        if weight != 0: # weight가 0이 아니면
            if (v == airports_name):  # 그리고 해당 도시에서 airport로 가는 길이 있으면
                airports_list.append(int(u)) # 해당 도시를 airport list에 추가한다.
            elif (u == airports_name):
                airports_list.append(int(v))
            else: # 만약 없으면 roads list에 v와 u를 추가한다.
                roads_list.append((int(v), int(u)))

    return roads_list, airports_list

print(development(4, test, test2))

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
