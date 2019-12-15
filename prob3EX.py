# -*- coding: utf-8 -*-
parent = {}
rank = {}

# https://debuglog.tistory.com/84
# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v) # v의 최상위 루트노드
    root2 = find(u) # u의 최상위 루트노드

    if root1 != root2: # v와 u의 최상위 루트노드가 같지 않으면
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]: # root 1의 랭크가 root2의 랭크보다 길면
            parent[root2] = root1 # root2의 부모가 root1이 된다.
        else: # 즉 긴 트리 밑에 짧은 트리를 갖다붙인다.
            parent[root1] = root2
            if rank[root1] == rank[root2]: # u와 v의 길이가 같으면
                rank[root2] += 1 # v의 랭크를 1 늘린다.

def kruskal(graph):
    for v in graph['vertices']:
        make_set(v) # 독립적인 집합으로 만들기

    mst = []

    edges = graph['edges']
    edges.sort()
    print(edges)

    for edge in edges:
        weight, v, u = edge
        # weight는 edge의 크기, v와 u는 엣지의 각각 노드 두 개

        if find(v) != find(u): # 두 노드의 최상위 정점이 같지 않으면
            union(v, u) # 두 노드를 잇고
            mst.append(edge) # 엣지를 연결함

    return mst

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ]
}
print(kruskal(graph))
