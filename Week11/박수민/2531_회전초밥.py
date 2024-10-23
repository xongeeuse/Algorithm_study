# 2531 회전초밥
# 1트

# import sys
# input = sys.stdin.readline
# from collections import deque

# N, d, k, c = map(int, input().split())
# # N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

# sushi = deque(int(input()) for _ in range(N))

# sushi_set = []

# for i in range(N):
#     dish = []
#     # 회전초밥 돌리면서 0부터 k-1 인덱스 세트 N개 만들기
#     su = set(list(sushi)[0:k])
#     if su in sushi_set:
#         continue
#     sushi_set.append(su)
#     sushi.rotate(-1)

# # 세트의 길이를 기준으로 내림차순 정렬 
# sort_sushi = sorted(sushi_set, key = lambda x: -len(x))
# max_len = len(sort_sushi[0])
# ans = max_len

# for i in range(len(sort_sushi)):
#     if len(sort_sushi[i]) < max_len:
#         continue
    
#     # 쿠폰으로 받을 스시가 스시 세트에 없을 떄
#     elif c not in sort_sushi[i]: 
#         ans += 1
#         break

# print(ans)



# 2트
# import sys
# input = sys.stdin.readline

# N, d, k, c = map(int, input().split())
# # N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

# sushi = [int(input()) for _ in range(N)]

# ans = 0

# for i in range(N):
#     dish = set()
#     for j in range(k):
#         dish.add(sushi[(i+j)%N])        
#     if len(dish) < ans:
#         continue
#     ans = len(dish)
#     if c not in dish:
#         ans = len(dish) +1

# print(ans)

# ...

# 3트
# import sys
# input = sys.stdin.readline
# from collections import deque

# N, d, k, c = map(int, input().split())
# # N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

# sushi = deque(int(input()) for _ in range(N))

# ans = 0

# for i in range(N):
#     # 초밥 회전시키면서 k만큼 인덱싱.
#     # 서비스 초밥 더해주고 set로 만듦
#     dish = set(list(sushi)[0:k]+[c])
#     sushi.rotate(-1)
#     # 현재 가짓수가 지금까지의 최대 가짓수보다 작으면 continue
#     if len(dish) < ans:
#         continue
#     # 현재 가짓수가 최대 가짓수가 되면 종료
#     if len(dish) == k+1:
#         ans = k+1
#         break
#     ans = len(dish)

# print(ans)
#
# 살려주세요

# pypy3로 통과 (...) 
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
# N: 접시 수, d: 초밥 가짓 수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호

sushi = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    # 서비스 초밥 set에 먼저 포함
    dish = set([c])
    for j in range(k):
        dish.add(sushi[(i+j)%N])        
    if len(dish) < ans:
        continue
    if len(dish) == k+1:
        ans = k+1
        break
    ans = len(dish)
    
print(ans)