# Sol - 강의보고 품 (순열 조합 공부 후 다시 풀기)

def my_dfs(n, A_li, B_li):
    global min_ans
    if n == N+1:
        if len(A_li) == M:
            A_sum = B_sum =  0
            for i in range(M):
                for j in range(M):
                    A_sum += arr[A_li[i]][A_li[j]]
                    B_sum += arr[B_li[i]][B_li[j]]
            min_ans = min(min_ans, abs(A_sum - B_sum))
        return

    my_dfs(n+1, A_li+[n], B_li)
    my_dfs(n+1, A_li, B_li+[n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N//2
    arr = [[0] + list(map(int, input().split())) for _ in range(N)]
    arr.insert(0, [0] * (N+1))
    min_ans = float('inf')
    my_dfs(1, [], [])
    print(f'#{tc} {min_ans}')