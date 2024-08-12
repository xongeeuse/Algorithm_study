T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    cnt = 1
    result = 1

    for i in range(len(carrots) - 1):
        if carrots[i] < carrots[i + 1]:
            cnt += 1
        else:
            cnt = 1
        result = cnt if result < cnt else result

    print(f'#{t}', result)