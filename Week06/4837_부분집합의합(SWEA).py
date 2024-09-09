# sol_1 - 내 풀이
# A 생성
size = 12
A = []
for temp in range(1, size+1):
    A.append(temp)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    subset_li = []
    cnt = 0

    for i in range(1 << size):
        subset = []
        for j in range(size):
            if i & (1 << j):
                subset.append(A[j])
        subset_li.append(subset)

    for i in range(1 << size):
        if len(subset_li[i]) == N and sum(subset_li[i]) == K:
            cnt += 1
    print(f'#{tc} {cnt}')

# # sol_2 - 문어박사 인강
# def my_dfs(n, sm, cnt):
#     global ans
#     # 가지치기: 가장 마지막에 고민.. 가장 위에 처리
#     if sm > K: # 이미 초과한 것 (음수가 없기 때문)
#         return
#
#     # 종료조건: n에 관련된 수식
#     if n == size: # 모든 숫자에 대해 다 돌았는데
#         if sm == K and cnt == N: # 합이 K이고
#             ans += 1
#         return
#
#     # 숫자를 사용하는 경우
#     my_dfs(n+1, sm+A[n], cnt+1)
#     # 숫자를 사용하지 않는 경우
#     my_dfs(n+1, sm, cnt)
#
# size = 12
# A = []
# for temp in range(1, size+1):
#     A.append(temp)
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#
#     ans = 0
#     my_dfs(0, 0, 0)
#     print(f'#{tc} {ans}')