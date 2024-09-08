import sys
sys.stdin = open('.txt')

T = int(sys.stdin.readline().strip())

numbers = [i for i in range(1, 13)]


def recur(start, total, cnt):
    global result

    if cnt == N:
        if total == K:
            result += 1
        return

    if start >= len(numbers):
        return

    recur(start + 1, total, cnt)
    recur(start + 1, total + numbers[start], cnt + 1)



for t in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().strip().split())       # N : 부분집합 중 N개의 원소 / K : 합이 K
    result = 0
    recur(0, 0, 0)
    print(f'#{t}', result)