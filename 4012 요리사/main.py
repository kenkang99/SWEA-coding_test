'''


N = 4인 예를 생각해보자. 시너지 Sij는 [Table 1]과 같이 주어진다.

(세로축으로 i번째 위치에 있고 가로축으로 j번째 위치에 있는 값이 Sij이다.)


                                                                      [Table 1]



식재료 1과 식재료 2를 A음식으로 만들고 식재료 3과 식재료 4를 B음식으로 만드는 경우를 생각하자.



1) 식재료 1을 식재료 2와 같이 요리했을 때 발생하는 시너지 S12는 5이다.

2) 식재료 2를 식재료 1과 같이 요리했을 때 발생하는 시너지 S21는 4이다.

3) A음식의 맛은 5 + 4 = 9가 된다.

4) 식재료 3을 식재료 4와 같이 요리했을 때 발생하는 시너지 S34는 3이다.

5) 식재료 4를 식재료 3과 같이 요리했을 때 발생하는 시너지 S43은 3이다.

6) B음식의 맛은 3 + 3 = 6이 된다.



따라서, 두 음식 간의 맛의 차이는 |9 – 6| = 3이 된다.



식재료 2와 식재료 4를 A음식으로 만들고 식재료 1과 식재료 3을 B음식으로 만드는 경우를 생각하자.



7) 식재료 2를 식재료 4와 같이 요리했을 때 발생하는 시너지 S24는 1이다.

8) 식재료 4를 식재료 2와 같이 요리했을 때 발생하는 시너지 S42는 2이다.

9) A음식의 전력은 1 + 2 = 3이 된다.

10) 식재료 1을 식재료 3과 같이 요리했을 때 발생하는 시너지 S13은 3이다.

11) 식재료 3과 식재료 1을 같이 요리했을 때 발생하는 시너지 S31은 2이다.

12) B음식의 맛은 3 + 2 = 5가 된다.



따라서, 두 음식간의 맛의 차이는 |3 – 5| = 2가 된다.

이 경우가 A음식과 B음식 간의 맛의 차이가 최소인 경우이다.

다른 경우에서는 맛의 차이가 2보다 작을 수 없다.

따라서, 본 예의 정답은 2가 된다.



 [제약사항]

1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3초

2. 식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)

3. 시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)

4. i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.



[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고,

그 다음 줄부터 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 식재료의 수 N이 주어진다.

다음 N개의 줄에는 N * N개의 시너지 Sij값들이 주어진다. i와 j가 서로 같은 경우는 0으로 주어진다.



[출력]

테스트 케이스 개수만큼 T개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t"로 시작하고 공백을 하나 둔 다음 정답을 출력한다. (t 는 1부터 시작하는 테스트 케이스의 번호이다.)

정답은 두 음식 간의 맛의 차이가 최소가 되도록 A음식과 B음식을 만들었을 때 그 차이 값이다.


'''

import sys
from itertools import combinations

sys.stdin=open('sample_input.txt')


T = int(input())

for test_case in range(1,T+1):

    N = int(input())

    map_list = [ list(map(int,input().split())) for _ in range(N)]

    ingredient_list= [ i for i in range(1,N+1) ]

    min_ans = 10000000000000000000

    '''
    식재료가 겹치면 안된다 <- 문제를 잘 읽어야하는 이유

    for comb1 in combinations(ingredient_list,2):
        for comb2 in combinations(ingredient_list,2):
            if comb1==comb2:
                continue

            comb1_taste = map_list[comb1[0]-1][comb1[1]-1] + map_list[comb1[1]-1][comb1[0]-1]
            comb2_taste = map_list[comb2[0]-1][comb2[1]-1] + map_list[comb2[1]-1][comb2[0]-1]

            min_ans = min(min_ans, abs(comb1_taste-comb2_taste))
    '''

    '''
    난독이슈<- 식재료 2개 고정이 아니었구나 샹
    for comb1 in combinations(ingredient_list,2):
        for comb2 in combinations(ingredient_list,2):
            if len(set(comb1+comb2)) != 4:     # 튜플 겹치는게 있는지
                continue

            comb1_taste = map_list[comb1[0]-1][comb1[1]-1] + map_list[comb1[1]-1][comb1[0]-1]
            comb2_taste = map_list[comb2[0]-1][comb2[1]-1] + map_list[comb2[1]-1][comb2[0]-1]

            min_ans = min(min_ans, abs(comb1_taste-comb2_taste))
    '''

    '''
    comb2는 여집합인데 이중for문 처리해서 시간 너무 잡아먹음

    count_ingredient = N // 2

    for comb1 in combinations(ingredient_list,count_ingredient):
        for comb2 in combinations(ingredient_list,count_ingredient):
            comb1_taste = 0
            comb2_taste = 0
            if len(set(comb1+comb2)) != N:     # 튜플 겹치는게 있는지
                continue

            else :
                for comb1_real in combinations(comb1,2):
                    comb1_taste += map_list[comb1_real[0]-1][comb1_real[1]-1] + map_list[comb1_real[1]-1][comb1_real[0]-1]
                for comb2_real in combinations(comb2,2):
                    comb2_taste += map_list[comb2_real[0]-1][comb2_real[1]-1] + map_list[comb2_real[1]-1][comb2_real[0]-1]

            min_ans = min(min_ans, abs(comb1_taste-comb2_taste))
    '''

    count_ingredient = N // 2

    for comb1 in combinations(ingredient_list,count_ingredient):
        comb2 = set(ingredient_list)-set(comb1)
        comb1_taste = 0
        comb2_taste = 0

        for comb1_real in combinations(comb1,2):
            comb1_taste += map_list[comb1_real[0]-1][comb1_real[1]-1] + map_list[comb1_real[1]-1][comb1_real[0]-1]
        for comb2_real in combinations(comb2,2):
            comb2_taste += map_list[comb2_real[0]-1][comb2_real[1]-1] + map_list[comb2_real[1]-1][comb2_real[0]-1]

        min_ans = min(min_ans, abs(comb1_taste-comb2_taste))


    print(f'#{test_case} {min_ans}')




