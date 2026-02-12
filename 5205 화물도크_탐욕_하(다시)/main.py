'''

 앞 작업의 종료와 동시에 다음 작업을 시작할 때, 최대 운용가능 개수

[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 신청서 N이 주어지고, 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s와 종료 시간 e가 주어진다.


1<=N<=100, 0<=s<24, 0 ＜ e ＜= 24

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''


# 사고과정
    # 시작시간으로 일단 정렬할까?
    # 아님 사용시간을 기준으로 정렬을 한 뒤에 백트래킹을 할까? <- 이게 맞을듯? <- 반례 = 효율적인 애들이 모두 같은 시간일때 + 아마 NxN 의 경우의 수 기준으로 해야돼서 시간초과날듯?
    # 수업 들어보니까 종료시간 기준으로 정렬이 맞네 <- 근데 이건 예외가 없나


import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    N = int(input())

    map_list = []

    for _ in range(N):
        map_list.append(list(map(int,input().split())))

    map_list.sort(key= lambda x: x[1])


    start,end = map_list[0][0],map_list[0][1]
    cnt=1
    for i in range(1,N):
        if map_list[i][0]< end:
            continue
        start,end = map_list[i][0], map_list[i][1]
        cnt+=1

    print(f'#{t} {cnt}')

