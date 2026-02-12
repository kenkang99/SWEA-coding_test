'''

주머니 당 사탕의 개수 제시
몇개 주머니 선택할지 K로 제시, K개 조합 중 최대 최소 적은애로
'''

import sys

sys.stdin=open('sin.txt')

T = int(input())

for t in range(1,T+1):
    N,K=map(int,input().split())

    coin_list = list(map(int,input().split()))

    coin_list.sort()

    ans = 10000000000000000000

    for k in range(K-1,N):
        ans = min(ans, coin_list[k] - coin_list[k - K +1])

    print(f'#{t} {ans}')