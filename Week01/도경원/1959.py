import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    temp = 0
    max_v = 0
    if n < m:
        for i in range(m-n+1):
            for j in range(n):
                temp += arr_1[j] * arr_2[j+i]
            if temp > max_v:
                max_v = temp
            temp = 0
    if n >= m:
        for i in range(n-m+1):
            for j in range(m):
                temp += arr_2[j] * arr_1[j+i]
            if temp > max_v:
                max_v = temp
            temp = 0
    print(f'#{tc} {max_v}')
