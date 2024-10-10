import sys
sys.stdin = open('input.txt')

# GPT 찬스..
# BFS로 다시 풀기...

from collections import deque

def bfs(N):
    q = deque()
    q.append(N)
    distance[N] = 0
    cnt[N] = 1  # 시작 위치에서의 경로 수는 1로 초기화

    while q:
        now = q.popleft()

        # 현재 좌표에서 이동할 수 있는 다른 좌표 확인
        for next in [now - 1, now + 1, now * 2]:
            if 0 <= next <= 100000:
                # 더 짧은 경로를 발견한 경우
                if distance[next] > distance[now] + 1:
                    distance[next] = distance[now] + 1
                    cnt[next] = cnt[now]  # 새로운 최단 경로 수를 현재 경로 수로 설정
                    q.append(next)

                # 동일한 최단 거리로 도달한 경우
                elif distance[next] == distance[now] + 1:
                    cnt[next] += cnt[now]  # 기존 경로 수에 현재 경로 수 추가

                # *2 이동의 경우 시간을 증가시키지 않기 때문에 별도 조건으로 처리 필요 없음?

    return cnt[K]

N, K = map(int, input().split())
INF = int(1e9)
distance = [INF] * 100001  # distance 초기값을 INF로 설정
cnt = [0] * 100001

result = bfs(N)

print(distance[K])
print(result)
