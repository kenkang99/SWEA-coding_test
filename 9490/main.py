import sys

sys.stdin = open('input1.txt')

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,(input().split()))

    ballon_list = []
    sum_list = [[0]*M for _ in range(N)]

    for i in range(N):
        ballon_list.append(list(map(int,input().split())))

    direcetion = [(1,0),(-1,0),(0,1),(0,-1)]
    answer = 0

    for i in range(N):
        for j in range(M):
            ballon_size=ballon_list[i][j]
            sum_list[i][j]=ballon_size

            for (dx,dy) in direcetion:
                for size in range(1,ballon_size+1):
                    now_x,now_y = i+size*dx, j+size*dy
                    if (now_x < 0 or now_x > N-1) or (now_y < 0 or now_y > M-1):
                        continue
                    else:
                        sum_list[i][j]+=ballon_list[now_x][now_y]

            if sum_list[i][j] > answer:
                answer = sum_list[i][j]

            else:
                pass

    print(f'#{test_case} {answer}')