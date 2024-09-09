import sys
sys.stdin = open('input.txt')

X = 12
A = list(range(1, X + 1))

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())        # N개의 원소, 원소의 합 K
    result = 0

    for i in range(1 << X):
        cnt, temp_sum = 0, 0
        for j in range(X):
            if i & (1 << j):
                cnt += 1
                temp_sum += A[j]
                if cnt > N:
                    break
        if cnt == N and temp_sum == K:
            result += 1

    print(f'#{tc}', result)
