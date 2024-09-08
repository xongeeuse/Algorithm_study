import sys

sys.stdin = open('.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # 연산자 DFS?