# sol_1 - for문 써서 윈도우 조정
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            # 윈도우 조정
            for x in range(M):
                for y in range(M):
                    sum_fly += arr[i+x][j+y]
                    if sum_fly > max_fly:
                        max_fly = sum_fly

    print(f'#{tc} {max_fly}')

# # sol_2 - 델타 탐색 사용
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     dxy = [(dx, dy) for dx in range(M) for dy in range(M)]
#     max_fly = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             sum_fly = 0
#             for dx, dy in dxy:
#                 sum_fly += arr[i+dx][j+dy]
#             if max_fly < sum_fly:
#                 max_fly = sum_fly
#     print(f'#{tc} {max_fly}')