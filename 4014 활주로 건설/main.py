'''
[제약사항]

1. 시간제한 : 최대 50 개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3 초

2. N 의 크기는 6 이상 20 이하의 정수이다. ( 6 ≤ N ≤ 20 )

3. 경사로의 높이는 항상 1 이고, 길이 X 는 2 이상 4 이하의 정수이다. ( 2 ≤ X ≤ 4 )

4. 지형의 높이는 1 이상 6 이하의 정수이다.

5. 동일한 셀에 두 개 이상의 경사로를 겹쳐서 사용할 수 없다.

( 아래 [Fig. 10] 과 같은 경우는 경사로를 설치하여 활주로를 연결 할 수 없다. )

6. 경사로는 세워서 사용할 수 없다. ( [Fig. 11] 참고 )


[입력]

입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,

그 다음 줄부터 T 개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 크기인 N 과 경사로의 길이 X 가 주어진다.

다음 N 개의 줄에는 N * N 크기의 지형 정보가 주어진다.




[출력]

테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.

각 줄은 "#t" 로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t 는 1 부터 시작하는 테스트 케이스의 번호이다. )

정답은 활주로를 건설할 수 있는 경우의 수이다.
'''


import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for test_case in range(1,T+1):

    N,X = map(int,input().split())

    map_list_row = [list(map(int,input().split())) for _ in range(N)]
    map_list_col = [ [0]*N for _ in range(N) ]

    for temp in map_list_row:
        temp.append(temp[-1]-1)

    for i in range(N):
        for j in range(N):
            map_list_col[i][j] = map_list_row[j][i]

    for temp in map_list_col:
        temp.append(temp[-1]-1)

    # 1분기 가로일때 세로일때
    # 2분기 순회하다가 달라질 때 2이상차이면 continue, X 번 이동 전에 달라지거나 벽이면 continue
    #

    print(map_list_row)
    print(map_list_col)



    def ans(map_list):
        ans = 0

        for row in map_list:
            count=1
            count_buffer = True

            for i in range(N):
                if row[i+1]==row[i]:


                elif row[i+1]==row[i]+1:


                elif row[i+1]==row[i]-1:

                else:
                    break

            if count_buffer:
               ans+=1

        return ans

    answer = ans(map_list_row) + ans(map_list_col)

    print(f'#{test_case} {answer}')



# transposed_matrix = list(map(list, zip(*matrix)))