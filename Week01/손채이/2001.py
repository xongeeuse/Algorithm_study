import sys

sys.stdin = open('2001_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            for k in range(M):
                for x in range(M):
                    cnt += arr[i + k][j + x]
            if result < cnt:
                result = cnt
    print(f'#{t} {result}')
