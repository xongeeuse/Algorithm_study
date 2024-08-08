import sys
sys.stdin = open('9386_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    result = 0
    cnt = 0

    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            result = cnt if cnt > result else result
        else:
            cnt = 0

    print(f'#{t} {result}')