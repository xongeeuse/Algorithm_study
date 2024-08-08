import sys
sys.stdin = open("input.txt", "r")

# T = int(input())  # 테스트 케이스 개수 입력
# for tc in range(1, T+1):  # 각 테스트 케이스에 대한 반복
#     n = int(input())  # 버스 노선 개수
#     temp = []  # 각 위치에 대한 카운트를 저장할 리스트
#     ans = []  # 결과를 저장할 리스트
#     for _ in range(n):
#         a, b = map(int, input().split())  # a이상 b이하인 정류장 이동 가능
#         if len(temp) < b:  # n번쨰 a, b를 입력받을때 a ~ b 구간이 0으로 초기화가 안되있는 경우 대비
#             for i in range(len(temp), b+1):
#                 temp += [0]
#         for i in range(a, b+1):  # a ~ b 구간 정류장 이동 가능하여 카운트
#             temp[i] += 1
#     p = int(input())
#     for _ in range(p):  # 정류장 개수
#         c = int(input())  # c번 정류장
#         ans += [temp[c]]  # 결과리스트에 넣기
#     print(f'#{tc}', *ans)
#     # print('#' + str(tc), ' '.join(map(str, ans)))

# 선생님이 고쳐준 코드
import sys
sys.stdin = open('s_input.txt')

T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T+1):  # 각 테스트 케이스에 대한 반복
    n = int(input())  # 버스 노선 개수
    temp = []  # 각 위치에 대한 카운트를 저장할 리스트
    ans = []  # 결과를 저장할 리스트
    for _ in range(n):
        a, b = map(int, input().split()) # a이상 b이하인 정류장 이동 가능
        if len(temp) < b:  # 처음 이후로 a, b를 입력받을때 a ~ b 구간이 초기화가 안되있는 경우 대비
            # for i in range(len(temp), b+1):
            for i in range(len(temp), 5001):
                temp += [0]
        for i in range(a, b+1):  # a ~ b 구간 정류장 이동 가능하여 카운트
            temp[i] += 1
    p = int(input())
    for _ in range(p):  # 정류장 개수
        c = int(input())  # c번 정류장
        ans += [temp[c]]  # 결과리스트에 넣기
    print(f'#{tc}', *ans)