N, d, k, c = map(int, input().split())
table = []
ans = 0

for i in range(N):
    table.append(int(input()))

for i in range(N):
    temp = set()
    for j in range(k):
        temp.add(table[(i+j)%N])
    temp.add(c) # 쿠폰에 있는 스시 추가

    if ans < len(temp):
        ans = len(temp)

print(ans)