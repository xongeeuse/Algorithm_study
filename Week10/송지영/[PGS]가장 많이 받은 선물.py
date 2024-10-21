# 몰르겠습니다...
# 담주부터 백준에서 문제 고를래..

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi",
         "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

N = len(friends)
data = [[0] * N for _ in range(N)]
idx_list = {friends[i] : i for i in range(N)}
print(idx_list)


for gift in gifts:
    a, b = gift.split()
    data[idx_list[a]][idx_list[b]] += 1

print(data)