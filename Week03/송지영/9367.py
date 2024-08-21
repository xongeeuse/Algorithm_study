import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    max_cnt = 0
    cnt = 1

    for i in range(N-1):
        if data[i] < data[i+1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{tc}', max_cnt)