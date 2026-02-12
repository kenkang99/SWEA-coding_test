'''

n개 집합

0 1 1은 뭐여


1367 24 5

'''

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    n,m = map(int,input().split())

    map_list = [i for i in range(n+1)]
    parent = map_list[:]

    def find(x):
        now_par = parent[x]

        if now_par==x:
            return x

        parent[x] = find(now_par)

        return parent[x]


    def union(x,y):
        par_x = find(x)
        par_y = find(y)

        if par_x != par_y:
            parent[par_y] = par_x


    a=[]

    for _ in range(m):
        now = list(map(int,input().split()))

        if now[0] == 0:
            union(now[1],now[2])

        else :
            if find(now[1]) == find(now[2]):
                a.append('1')
            else:
                a.append('0')

    b = ''.join(a)

    print(f'#{t} {b}')