'''

1 -> N -> 1까지 이동하기

최소비용 구하기
출발,도착 기준 비용다름
각 구역 한번씩만 돌아야함

사고과정 : 탐색 타다가 이미 최소값후보보다 값이 크면 가지치자(비용은 최소 0이상이기 때문)
근데 어케 갔다가 돌아오고 최신화하지 <- visited를 상황마다 어떻게 적용하지
'''

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def search(start,sub_total):
    global min_val

    if False not in visit:
        min_val=min(min_val,sub_total+map_list[start][0])

    else:
        for end in range(N):
            if start != end and visit[end] == False:
                sub_total += map_list[start][end]
                #start = end

                if sub_total >= min_val:
                    return

                visit[end] = True

                search(end,sub_total)

                visit[end] = False
                sub_total -= map_list[start][end]


for test_case in range(1,T+1):
    N = int(input())

    map_list = [list(map(int,input().split())) for _ in range(N)]

    min_val = 100000000

    visit = [False]*N

    visit[0]=True

    search(0, 0)

    print(f'#{test_case} {min_val}')




