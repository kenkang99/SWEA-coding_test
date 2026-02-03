import sys

sys.stdin = open('input1.txt')

T = int(input())

'''
1 발견 인덱스 기준 +(k-1)까지는 모두 1, +k 는 벽이거나 0
'''
for test_case in range(1,T+1):
    N, K = map(int, input().split())

    map_list = [ [0]*(N+1) ]


    # N x N이 아니라 N+1 x N+1 로 테두리 모두 0 추가해야할듯?

    for i in range(1,N+1):
        map_list.append([0])
        map_list[i].append(map(int,input().split()))

    print(map_list)

    answer = 0

    # 이것도 순서대로 우,하 일자로? 했을 때 카운트못할일이 있나
    # 1 1 1 1 0 이때는 우하로만 탐색하면 계산 잘못함 <- 이것만 해결하면 되는데

    for i in range(N+1 - K):
        for j in range(N+1 - K):
            if map_list[i][j] == 1 :
                continue # 0은 스킵
            else :
                for row in range(1,K+1):
                    if (j+row) == N or map_list[i][j+row] == 0:
                        break

                    if row==K:
                        if (j+row+1) == N or map_list[i][j+row+1] == 0:
                            answer +=1

                        else:
                            pass

                for col in range(1, K+1):
                    if (i+col) == N or map_list[i + col][j] == 0:
                        break

                    if col == K:
                        if (i + col + 1) == N or map_list[i + col + 1][j] == 0:
                            answer += 1
                        else:
                            pass

    print((f'#{test_case} {answer}'))