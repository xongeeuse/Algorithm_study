from itertools import combinations, permutations
'''
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''

# 두 그룹의 차이를 최소화하는 함수
def min_difference(N, board):
    # 1부터 N까지의 숫자 리스트를 생성 (재료 번호: [1, 2, 3, 4])
    ingredient_list = [x + 1 for x in range(N)]

    # N // 2개의 재료를 고르는 모든 조합을 생성 (예: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
    ingredient_combination = list(combinations(ingredient_list, N // 2))

    # 차이의 최소값을 저장할 변수 (초기값은 매우 큰 수)
    min_difference = 1e9

    # 조합의 절반만 계산 (조합의 대칭성 활용)
    # 4개 식재료가 있을 때, (1, 2) (3, 4)는 (3, 4) (1, 2)와 동일
    for i in range(len(ingredient_combination) // 2):
        foodA = 0  # A팀의 점수
        foodB = 0  # B팀의 점수

        # A팀에서 2개씩 순서 있게 뽑는 모든 순열 생성
        # 예: i=0일 때 A팀: (1, 2), B팀: (3, 4)
        select_two_A = list(permutations(ingredient_combination[i], 2))
        # A팀 순열: [(1, 2), (2, 1)]

        select_two_B = list(permutations(ingredient_combination[len(ingredient_combination) - i - 1], 2))
        # B팀 순열: [(3, 4), (4, 3)]

        # A팀의 순열에 해당하는 점수 합산
        # board[1][2] = 5, board[2][1] = 4
        for k in range(len(select_two_A)):
            foodA += board[select_two_A[k][0]][select_two_A[k][1]]  # A팀 점수: 5 + 4 = 9

        # B팀의 순열에 해당하는 점수 합산
        # board[3][4] = 3, board[4][3] = 3
        for l in range(len(select_two_B)):
            foodB += board[select_two_B[l][0]][select_two_B[l][1]]  # B팀 점수: 3 + 3 = 6

        # 두 팀의 점수 차이를 계산 (abs(9 - 6) = 3)
        difference = abs(foodA - foodB)

        # 차이가 더 작다면 최소값을 갱신
        if min_difference > difference:
            min_difference = difference  # 현재 최소 차이: 3

    # 최소 차이를 반환
    return min_difference


T = int(input())

for tc in range(1, T + 1):
    # 식재료의 수 입력
    N = int(input())  # 4

    # N x N 크기의 식재료 간 맛 점수 표 생성
    # board:
    # 0 5 3 8
    # 4 0 4 1
    # 2 5 0 3
    # 7 2 3 0
    board = [[0] * (N + 1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]

    # 결과 출력 (테스트 케이스 번호와 최소 차이 값)
    # #1 2
    print("#{} {}".format(tc, min_difference(N, board)))