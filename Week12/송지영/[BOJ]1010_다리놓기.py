import sys
sys.stdin = open('input.txt')

def bridge(N, M):
    # dp[i][j] = 서쪽에 i개, 동쪽에 j개의 사이트가 있을 때 가능한 경우의 수
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    # 서쪽에 1개의 사이트가 있으면
    # 동쪽의 사이트 수만큼 다리 놓을 수 있음
    for i in range(1, M + 1):
        dp[1][i] = i

    # 서쪽 사이트부터 하나씩 증가, 1은 이미 위에서 처리함
    for i in range(2, N + 1):
        # 동쪽 사이트 i ~ M까지 증가, 항상 서쪽보다 커야 함
        for j in range(i, M + 1):
            # 현재 고려 중인 동쪽 사이트의 위치
            # j부터 i까지 역순으로 반복
            for k in range(j, i - 1, -1):
                # dp[i - 1][k - 1]: i번째 서쪽 사이트를 k번째 동쪽 사이트와 연결했을 때,
                # 남은 사이트들로 만들 수 있는 경우의 수
                # 다 더하면 모든 경우의 수.....?
                dp[i][j] += dp[i - 1][k - 1]

    return dp[N][M]

for _ in range(int(input())):
    N, M = map(int, input().split())        # 서쪽에 N개, 동쪽에 M개의 사이트
    print(bridge(N, M))