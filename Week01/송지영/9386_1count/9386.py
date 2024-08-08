import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, list(input())))

    max_cnt = 0
    cnt = 0

    for num in nums:
        if num == 1:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f'#{tc}', max_cnt)