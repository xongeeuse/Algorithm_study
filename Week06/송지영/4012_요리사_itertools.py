import sys
sys.stdin = open('input.txt')
'''
dfs 돌려서 N//2개 재료 선택 완료하면
그 값으로 시너지 비교해도 되겠으나 걍 itertools 씀
'''

import itertools

def get_synergy(A):
    global result

    combi_B = []
    for i in ingredients:
        if i not in combi_A:
            combi_B.append(i)

    # 조합 내에서 순열 만들어서 시너지 더하기
    permu_A = list(itertools.permutations(combi_A, 2))
    permu_B = list(itertools.permutations(combi_B, 2))

    synergy_A, synergy_B = 0, 0
    for i, j in permu_A:
        synergy_A += data[i][j]
    for i, j in permu_B:
        synergy_B += data[i][j]

    if result > abs(synergy_A - synergy_B):
        result = abs(synergy_A - synergy_B)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    ingredients = list(range(N))
    combis = list(itertools.combinations(ingredients, N // 2))

    for combi_A in combis:
        get_synergy(combi_A)

    print(f'#{tc}', result)

