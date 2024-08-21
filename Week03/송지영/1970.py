import sys
sys.stdin = open('input.txt')
type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = []
    for t in type:
        cnt = 0
        while N >= t:
            cnt = N // t
            N %= t
        result.append(cnt)

    print(f'#{tc}')
    print(*result)
