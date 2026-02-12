'''

1번-2번, 1번-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

[입력]

첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M, 다음 줄에 M 쌍의 번호가 주어진다. 2<=N<=100, 1<=M<=100

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



'''
# M만큼 쌍 묶고
# 서로소면 묶기 x 서로소 아니면 묶기

import sys

sys.stdin=open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())

    # 한줄로 받을 때부터 한쌍으로 묶기 가능한가
    coup_list = list(map(int,input().split()))

    later_sum = N - len(set(coup_list))

    coup_set=set()

    for i in range(0,len(coup_list),2):
        coup_set.add(coup_list[i:i+2])

    for i in range(M):
        for j in range(i,M):
            if coup_set[i] & coup_set[j]:
                temp = coup_set[i] | coup_set[j]

    # 답은 N - set(coup_list) + 세트 개수

import sys

# 테스트용 입력 설정 (실제 제출 시 삭제)
# sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))

    # 그룹들을 담을 리스트 (각 요소는 set)
    groups = []

    # 1. 들어오는 쌍(pair)을 하나씩 처리
    for i in range(0, len(pairs), 2):
        u, v = pairs[i], pairs[i + 1]

        # 이 쌍(u, v)와 연결된 기존 그룹들을 찾음
        related_group_indices = []

        for idx, group in enumerate(groups):
            # 교집합이 하나라도 있으면 연결된 그룹임
            if u in group or v in group:
                related_group_indices.append(idx)

        # 2. 찾은 그룹들을 다 합치고 + 새 쌍도 추가
        if not related_group_indices:
            # 겹치는 게 없으면 새 그룹 생성
            groups.append({u, v})
        else:
            # 겹치는 그룹이 있다면, 그 그룹들을 전부 하나로 합쳐야 함
            new_combined_group = {u, v}

            # 뒤에서부터 꺼내야 인덱스가 안 꼬임 (pop 사용 시 중요!)
            for idx in sorted(related_group_indices, reverse=True):
                new_combined_group.update(groups.pop(idx))

            groups.append(new_combined_group)

    # 3. 그룹에 속하지 않은(혼자 남은) 사람 처리
    # 전체 사람 수 - 그룹에 속한 사람 수 + 그룹의 개수
    people_in_groups = set()
    for g in groups:
        people_in_groups.update(g)

    # 그룹 개수 + 독도(혼자 있는 사람) 수
    ans = len(groups) + (N - len(people_in_groups))

    print(f"#{t} {ans}")