import sys
from collections import deque

sys.stdin=open('input.txt')


T=10

for t in range(1,T+1):
    input()

    map_list = [input() for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]


    
    for i in range(16):
        if map_list[i].find('2') != -1:
            start = (i,map_list[i].find('2'))
        if map_list[i].find('3') != -1:
            end = (i,map_list[i].find('3'))


    dir_list = [(-1,0),(0,1),(1,0),(0,-1)]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    ans=0

    while queue:
        x, y = queue.popleft()

        for dx,dy in dir_list:
            now_x,now_y = x+dx, y+dy

            if (now_x,now_y) == end:
                ans = 1
                break

            elif now_x>=0 and now_y>=0 and now_x<=15 and now_y<=15 and map_list[now_x][now_y]=='0' and visited[now_x][now_y]==False:
                queue.append((now_x,now_y))
                visited[now_x][now_y]=True

    print(f'#{t} {ans}')