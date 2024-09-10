#  오른쪽 위에 올라가 있는 무게의 총합이 왼쪽에 올라가 있는 무게의 총합보다 더 커져서는 안 된다.

import itertools

def check(N, weight):
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))


# 지피티
# import itertools
#
#
# def count_valid_configurations(N, weights):
#     valid_count = 0
#
#     # 모든 무게 추의 순열을 생성
#     permutations = itertools.permutations(weights)
#
#     for perm in permutations:
#         # 비트마스크를 사용하여 무게 추를 왼쪽 또는 오른쪽에 배치
#         total_configurations = 1 << N  # 2^N 가지 가능한 조합
#         for mask in range(total_configurations):
#             left_sum = 0
#             right_sum = 0
#             for i in range(N):
#                 if mask & (1 << i):
#                     right_sum += perm[i]
#                 else:
#                     left_sum += perm[i]
#             # 현재 조합이 유효한지 확인
#             if right_sum <= left_sum:
#                 valid_count += 1
#
#     return valid_count
#
#
# # 입력 받기
# T = int(input())
# results = []
#
# for _ in range(T):
#     N = int(input())
#     weights = list(map(int, input().split()))
#     result = count_valid_configurations(N, weights)
#     results.append(result)
#
# # 결과 출력
# for result in results:
#     print(result)