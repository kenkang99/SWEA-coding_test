'''

[입력]


첫 번째 줄에 테스트 케이스의 수 T가 주어진다.


각 테스트 케이스의 첫 번째 줄에는 재료의 수, 제한 칼로리를 나타내는 N, L(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)가 공백으로 구분되어 주어진다.


다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는 Ti, Ki(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)가 공백으로 구분되어 주어진다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력한다.


민기식 다이어트 제한 칼로리에서 최대 점수 뽑는 조합

이것도 백트래킹하면 될듯
'''

# import sys
# import heapq
#
# sys.stdin = open('sample_input.txt')
#
# T = int(input())
#
# def search(now,sub_cal,good):
#     global ans_max
#
#     if False not in visited:
#         ans_max = max(ans_max, good)
#
#     for i in range(N):
#         if visited[i]==False:
#             if sub_cal+food_list[now][1]>L:
#                 ans_max = max(ans_max, good)
#                 return
#
#             sub_cal+=food_list[now][1]
#             good+=food_list[now][0]
#
#             visited[i] = True
#             search(i,sub_cal,good)
#
#             # 백트래킹
#             visited[i] = False
#             sub_cal -= food_list[now][1]
#             good -= food_list[now][0]
#
#
# for t in range(1,T+1):
#     N, L = map(int,input().split())
#
#     food_list = []
#
#     # 정렬이 더 빠를까 그냥 하는게 더 빠를까
#     # 정렬 안해서 틀린듯? 근데 칼로리정렬 힙으로 어케 하지 평소처럼 하지말고 따로 받자
#     for _ in range(N):
#         good,cal = map(int,input().split())
#         heapq.heappush(food_list,(cal,good))
#         #food_list.append(list())
#
#     ans_max = 0
#
#     for i in range(N):
#         visited = [False] * N
#         visited[i]=True
#
#         search(i,0,0)
#
#     print(f'#{t} {ans_max}')
#


import sys
import heapq

sys.stdin = open('sample_input.txt')

T = int(input())


def search(now, start, sub_cal, good):
    global ans_max

    if now==start:
        search(now+1,start, sub_cal, good)

    if sub_cal + food_list[now][0] > L or now == N-1:
        ans_max = max(ans_max, good)
        return

    else:
        sub_cal += food_list[now][0]
        good += food_list[now][1]

        search(now+1,start, sub_cal, good)

            #
            # # 백트래킹
            # visited[i] = False
            # sub_cal -= food_list[now][1]
            # good -= food_list[now][0]


for t in range(1, T + 1):
    N, L = map(int, input().split())

    food_list = []

    # 정렬이 더 빠를까 그냥 하는게 더 빠를까
    # 정렬 안해서 틀린듯? 근데 칼로리정렬 힙으로 어케 하지 평소처럼 하지말고 따로 받자
    for _ in range(N):
        good, cal = map(int, input().split())
        # heapq.heappush(food_list, (cal, good))
        food_list.append((cal,good))

    food_list.sort()
    # 걍 정렬쓰느게 낫겠다

    ans_max = 0

    for i in range(N):
        search(0,i ,0, 0)

    print(f'#{t} {ans_max}')
