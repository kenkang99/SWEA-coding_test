'''


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi, 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.

1<=N, M<=100, 1<=wi, ti<=50

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


트럭당 한 개의 컨테이너를 운반 가능


'''

# 큰 컨테이너 큰화물에 갖다박으면 끝? 반례 있을까 <- 없을듯?

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())

    contain = list(map(int,input().split()))
    contain.sort(reverse=True)

    truck = list(map(int,input().split()))
    truck.sort(reverse=True)

    idx = 0
    ans = 0

    for con in contain:
        if con <= truck[idx]:
            ans+=con
            idx += 1
            if idx == len(truck):
                break


    print(f'#{t} {ans}')
