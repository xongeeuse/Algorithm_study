N, D, K, C = map(int, input().split())  # N: 접시 수, D: 초밥의 가짓수, K: 연속해서 먹는 접시 수, C: 쿠폰 번호
data = []

for _ in range(N):
    data.append(int(input()))

result = -1

for i in range(N):
    if i <= N - K:
        pick = set(data[i:i + K])
    else:
        # pick = set(data[i:])
        # pick.update(data[:(i + K) % N])
        pick = set(data[i:]) | set(data[:(i + K) % N])


    pick.add(C)
    cnt = len(pick)

    # 고른 접시가 모두 다른 종류 + C 라면 그게 최댓값이니까 종료
    if cnt == K + 1:
        result = cnt
        break

    if result < cnt:
        result = cnt

print(result)










# 시간 초과!!!!!!!
# result = -1
#
# for i in range(N):
#     pick = set()
#     for j in range(K):
#         pick.add(data[(i + j) % N])
#
#     if C not in pick:
#         cnt = len(pick) + 1
#     else:
#         cnt = len(pick)
#
#     # 고른 접시가 모두 다른 종류고 + 지금까지 고른 접시에 C가 없으면 그게 최댓값이니까 종료
#     if cnt == K + 1:
#         result = cnt
#         break
#
#     if result < cnt:
#         result = cnt
#
# print(result)