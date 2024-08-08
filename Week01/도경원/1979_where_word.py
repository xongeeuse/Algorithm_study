import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 오류 3개 정도 남
# T = int(input())
# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     a = [[0] * (n+2)]
#     a += [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
#     a += [[0] * (n+2)]
#     cnt = 0
#     ans = 0
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if a[i][j] == 1 and cnt < k:
#                 cnt += 1
#             elif a[i][j] == 0:
#                 cnt = 0
#             if cnt == k:
#                 if a[i][j+1] == 1:
#                     cnt = 0
#                 elif a[i][j+1] != 1:
#                     ans += 1
#         cnt = 0
#     for j in range(1, n+1):
#         for i in range(1, n+1):
#             if a[i][j] == 1 and cnt < k:
#                 cnt += 1
#             elif a[i][j] == 0:
#                 cnt = 0
#             if cnt == k:
#                 if a[i+1][j] == 1:
#                     cnt = 0
#                 elif a[i+1][j] != 1:
#                     ans += 1
#         cnt = 0
#     print(f'#{tc}', ans)

# T = int(input())
# for tc in range(1, T + 1):
#     n, k = map(int, input().split())
#     a = [[0] * (n + 2)]
#     a += [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
#     a += [[0] * (n + 2)]
#     ans = 0
#
#     # 가로 방향 검사
#     for i in range(1, n + 1):
#         cnt = 0
#         for j in range(1, n + 1):
#             if a[i][j] == 1:
#                 cnt += 1
#             if a[i][j] == 0 or j == n:
#                 if cnt == k:
#                     ans += 1
#                 cnt = 0
#
#     # 세로 방향 검사
#     for j in range(1, n + 1):
#         cnt = 0
#         for i in range(1, n + 1):
#             if a[i][j] == 1:
#                 cnt += 1
#             if a[i][j] == 0 or i == n:
#                 if cnt == k:
#                     ans += 1
#                 cnt = 0
#
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # 가로 방향 검사
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 1:
                cnt += 1
            if a[i][j] == 0 or j == n-1:
                if cnt == k:
                    ans += 1
                cnt = 0

    # 세로 방향 검사
    for j in range(n):
        cnt = 0
        for i in range(n):
            if a[i][j] == 1:
                cnt += 1
            if a[i][j] == 0 or i == n-1:
                if cnt == k:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')