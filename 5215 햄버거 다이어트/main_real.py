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
# 이거 비트마스킹형식으로 푸는거 포스팅하는거 좋을듯


import sys

sys.stdin = open('sample_input.txt')

T = int(input())

def search(now,sub_cal,good):
    global ans_max

    # if now == N-1:
    #     ans_max = max(ans_max, good)
    #     return
    #
    # else:
    for i in range(now+1,N):
        #if visited[i]==False:
            if sub_cal+food_list[i][0] > L: # 칼로리 넘어가면 이전까지의 taste 점수와 max값 계산
                ans_max = max(ans_max, good)
                return

            sub_cal+=food_list[i][0]
            good+=food_list[i][1]

            if i == N-1 :
                ans_max = max(ans_max, good)
                return
            else:
                #visited[i] = True
                search(i,sub_cal,good) # 다음꺼 고고

                # 백트래킹
                #visited[i] = False
                sub_cal -= food_list[i][0]
                good -= food_list[i][1]



for t in range(1,T+1):
    N, L = map(int,input().split())

    food_list = []

    # 정렬이 더 빠를까 그냥 하는게 더 빠를까
    # 정렬 안해서 틀린듯? 근데 칼로리정렬 힙으로 어케 하지 평소처럼 하지말고 따로 받자 <- 이게 개소리였음, 우선순위큐 언제 쓰는지 확정을 잘 짓자

    for _ in range(N):
        good,cal = map(int,input().split())
        food_list.append((cal,good))

    food_list.sort()

    ans_max = 0

    for i in range(N):

        #visited = [False] * N
        #visited[i]=True

        if food_list[i][0] > L:
            break
        elif i==N-1:
            ans_max = max(ans_max,food_list[i][1])

        search(i,food_list[i][0],food_list[i][1])


    print(f'#{t} {ans_max}')

