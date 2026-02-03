'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.

김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.

사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.

방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.


[제약 사항]

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

[입력]

입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.
'''

import sys

sys.stdin = open('input.txt')



for test_case in range(1,11):

    T = int(input())
    map_list = [[0]*102 for i in range(100)] # 리스트 컴프리헨션 큰 차이 없음

    # for i in range(100):
    #     map_list.append(list(map(int,input().split())))  # 이것도 뭔가 양 옆에 0을 박아야 index out of error 발생하지 않을듯

    for i in range(100): # 이렇게 넣는 것보다 효율적인게 뭘까
        temp_list = list(map(int,input().split()))
        for j in range(1,101):
            map_list[i][j] = temp_list[j-1]

    # 2지점 인덱스 찾기 - find? <- 이건 문자열 용이고, .index를 사용해야함
    start_j = map_list[-1].index(2)


    # 위로 올라가다가 양옆에 1이 있는 경우 경로변경
    def up(i,j):
        up_i = i-1

        if up_i == 0:
            return j-1

        elif map_list[up_i][j+1]==1:
            return parrel(up_i,j,'right')

        elif map_list[up_i][j-1]==1:
            return parrel(up_i,j,'left')

        else:
            return up(up_i,j)

    # 양옆으로 가다가 위에 1이 있는 경우 경로변경
    def parrel(i,j,direct):
        try:
            if direct=='left':
                next_j=j-1
            elif direct=='right':
                next_j=j+1

            if map_list[i-1][next_j]==1:   # up(i-1, next_j로 하면 연속변환인 애는 취급못함
                return up(i,next_j)

            else:
                return parrel(i,next_j,direct)
        except:
            print(i,j,direct)


    print(f'#{test_case} {up(100,start_j)}')