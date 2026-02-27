'''

[입력]

가장 첫 번째 줄에는 전체 test case의 수 T(1≤T≤10)가 주어진다.

각 케이스의 첫째 줄에는 정점의 개수 V(1≤V≤100,000)와 간선의 개수 E(1≤E≤200,000)가 주어진다.

다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.

이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.

C는 음수일 수도 있으며, 절대값이 1,000,000을 넘지 않는다.


[출력]

각 테스트케이스마다 한 줄에 걸쳐, 테스트케이스 수 “#(테스트케이스 번호) “를 출력하고,  최소 스패닝 트리의 가중치를 출력한다.

'''

# 그냥 최소신장트리 구현하기

import sys

T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())

    dist_list=[list(map(int,input().split())) for _ in range(E)]

    node_list = [i for i in range(1,V+1)]
    par_list = [i for i in range(1, V + 1)]

    dist_list.sort(key = lambda x : x[2])

    def find(x):
        if x != par_list[x]:
            par_list[x] = find(par_list[x])
        return par_list[x]

    def union(x,y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:



    for item in dist_list:
