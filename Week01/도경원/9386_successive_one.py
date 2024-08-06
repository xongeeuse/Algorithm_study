T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input()))
    cnt, ans = 0, 0
    for aa in a:
        if aa == 1:
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0

    print(f'#{tc} {ans}')

