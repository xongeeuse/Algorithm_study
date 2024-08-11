import sys
sys.stdin = open("input.txt", "r")

# # sol 1
# T = int(input())
# for t in range(T):
#     n, m = map(int, input().split())
#     matrix = []
#     for _ in range(n):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     answer = 0
#     for i in range(n+1-m):
#         for j in range(n+1-m):
#             total = 0
#             for a in range(m):
#                 for b in range(m):
#                     total = total + matrix[i+a][j+b]
#             if answer < total:
#                 answer = total
#     print(f'#{t+1} {answer}')

# sol2 입력방식 변경
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    # matrix = []
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n+1-m):
        for j in range(n+1-m):
            temp = 0
            for a in range(m):
                for b in range(m):
                    temp += matrix[i+a][j+b]
            if answer < temp:
                answer = temp
    print(f'#{tc} {answer}')