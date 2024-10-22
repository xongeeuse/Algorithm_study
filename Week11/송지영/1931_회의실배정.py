N = int(input())    # N : 회의 수
data = []           # (회의 시작, 종료 시간) 저장할 리스트 생성
for _ in range(N):
    S, E = map(int, input().split())
    data.append((S, E))

# 회의 종료시간 기준으로 재정렬
# data.sort(key=lambda x: (x[1]))
data.sort(key=lambda x: (x[1], x[0]))
result, now_end = 0, 0

for start, end in data:
    if now_end <= start:
        now_end = end
        result += 1

print(result)





# deque ver.
# 시간 아주 조금 적게 걸리지만 굳이

# from collections import deque
#
# data = deque(data)
#
# while data:
#     start, end = data.popleft()
#     # 다음 회의 후보의 시작시간이 기존 회의의 종료시간과 같거나 그 이후라면
#     if now_end <= start:
#         now_end = end
#         result += 1     # 결과에 +1 하고
#
# print(result)