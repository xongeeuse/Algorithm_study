import sys
sys.stdin = open('input.txt')

import itertools

def dfs(cnt, left, right):
    global result

    if right > left:        #오른쪽 무게의 합이 왼쪽보다 크면 리턴
        return

    if cnt == N:            # 저울에 N개의 무게 추 모두 올렸고 왼쪽이 더 무겁다면
        result += 1         # 결과에 카운트하고 리턴
        return

    # 시간초과 나버려..검색찬스!
    # 백트래킹 추가인데 여기 넣는게 아닌가봐
    # 아니 맞네
    if left > total // 2:       # 왼쪽 무게의 합이 총 무게의 절반을 넘으면
        n = N - cnt             # 남은 경우의 수 계산해서
        result += (2 ** n)      # 결과에 합산해버리고 리턴
        return

    dfs(cnt + 1, left + permu[cnt], right)       # 왼쪽에 올리는 경우
    dfs(cnt + 1, left, right + permu[cnt])       # 오른쪽에 올리는 경우




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    total = sum(data)
    result = 0
    permus = list(itertools.permutations(data))
    for permu in permus:
        dfs(0, 0, 0)

    print(f'#{tc}', result)
