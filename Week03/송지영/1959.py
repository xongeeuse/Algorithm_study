import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data_A = list(map(int, input().split()))
    data_B = list(map(int, input().split()))

    # 항상 M을 크게 둘 것!
    if N > M:
        N, M, data_A, data_B = M, N, data_B, data_A

    max_sum = 0

    for i in range(M - N + 1):
        temp = 0
        sliced_B = data_B[i : N + i]
        for j in range(N):
            temp += data_A[j] * sliced_B[j]
        if max_sum < temp:
            max_sum = temp

    print(f'#{tc}', max_sum)
