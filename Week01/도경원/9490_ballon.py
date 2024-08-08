T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans, temp = 0, 0
    for i in range(n):
        for j in range(m):
            temp = a[i][j]
            temp_2 = temp
            for k in range(4):
                for l in range(1, temp + 1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < n and 0 <= nj < m:
                        temp_2 += a[ni][nj]
            if temp_2 > ans:
                ans = temp_2
    print(f'#{tc}', ans)