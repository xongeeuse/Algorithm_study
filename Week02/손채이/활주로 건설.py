import sys

sys.stdin = open('input.txt')

T = int(input())

def slope_check(array):
    pass

for t in range(1, T + 1):
    N, slope = map(int, input().split())
    tmp = []

    arr = [list(map(int, input().split())) for _ in range(N)]


    # 행
    for i in range(len(arr)):
        slope_check(arr[i])

    # 열
    # for j in range(len(arr)):
        # for i in range(len(arr[j])):

    '''
    [2, 2, 3, 2, 2, 2]
    행 or 열 탐색을 할 때 그 중 제일 큰 값 구하고,
    앞 뒤로 있는 값이 큰 값의 길이 (ex 1) 보다 크고 slope보다 길이가 크거나 같은 경우
    비탈길 가능?
    '''

