T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [[0] * (m+2)]
    a += [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    a += [[0] * (m+2)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            temp = a[i][j] + a[i][j+1] + a[i+1][j] + a[i][j-1] + a[i-1][j]
            if temp > ans:
                ans = temp

    print(f'#{tc}', ans)

