import sys
sys.stdin = open('input.txt')

T = int(input())

# My SOL
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    for i in range(N // 2):
        for x in range((N // 2) - 1 - i, -1, -1):
            data[i].pop()
            data[i].pop(0)

    for i in range((N // 2) + 1, N):
        for x in range(1, i - (N // 2) + 1):
            data[i].pop()
            data[i].pop(0)

    result = 0
    for i in range(N):
        for j in range(len(data[i])):
            result += data[i][j]

    print(f'#{tc}', result)




# # another SOL
# for tc in range(1, T + 1):
#     n = int(input())
#     data = [list(map(int, input())) for _ in range(n)]
#     start, end = n // 2, n // 2                             # 중간값 start, end에 할당
#
#     result = 0
#     for i in range(n):
#         for j in range(start, end + 1):
#             result += data[i][j]
#
#         if i < n // 2:                                      # 현재 i가 중간값보다 작을 경우
#             start -= 1                                      # start 1 감소
#             end += 1                                        # end 1 증가
#         else:                                               # 현재 i가 중간값보다 큰 경우
#             start += 1                                      # start 1 증가
#             end -= 1                                        # end 1 감소
#
#     print(f'#{tc}', result)