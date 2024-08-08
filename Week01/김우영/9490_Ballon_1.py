# sol_1
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 합을 담기 위한 리스트
    sum_list = []
    # 델타 검색하기 위한 좌표 리스트 (우, 하, 좌, 상)
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # arr를 제로 패딩하며 입력 받음
    arr = [[0] * (M+2)]
    arr += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    arr += [[0] * (M+2)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            temp_sum = arr[i][j]
            pang = arr[i][j] # 몇 개씩 터트릴지
            for dx, dy in dxy:
                for area in range(1, pang+1):
                    nx = i + dx * area
                    ny = j + dy * area
                    if nx < 0 or nx > N+1 or ny < 0 or ny > M+1:
                        continue
                    temp_sum += arr[nx][ny]
            sum_list.append(temp_sum)

    ans = max(sum_list)

    print(f'#{tc} {ans}')

    T = int(input())
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# # sol_2 - 방법은 같음, 간단히 나타낸 것
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) + [0] for _ in range(N)]
#     pang_max = 0
#     for i in range(N):
#         for j in range(M):
#             pang_sum = arr[i][j] # 자기 자신을 합의 기본 값으로
#             for k in range(1, arr[i][j] + 1):
#                 for dx, dy in dxy: # 4방향을 탐색하겠다.
#                     nx = i + dx*k
#                     ny = j + dy*k
#                     if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
#                         continue
#                     pang_sum += arr[nx][ny]
#             if pang_max < pang_sum:
#                 pang_max = pang_sum
#     print(f'#{tc} {pang_max}')