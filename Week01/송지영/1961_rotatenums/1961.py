import sys
sys.stdin = open('input.txt')

# 90도 회전하는 함수
def rotate(arr):
    pre_result = []
    result = []

    for j in range(N):
        for i in range(N):
            pre_result.append(arr[N-i-1][j])

    for i in range(N):
        result.append(pre_result[N * i:i * N + N])

    return result


# 함수 다시
# def rotate(arr):
#     result = [[0] * N for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             result[i][j] = arr[N-j-1][i]
#
#     return result



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    r90 = rotate(arr)
    r180 = rotate(r90)
    r270 = rotate(r180)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(r90[i]), ''.join(r180[i]), ''.join(r270[i]))



