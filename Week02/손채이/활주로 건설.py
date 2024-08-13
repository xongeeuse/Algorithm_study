import sys

sys.stdin = open('input.txt')

T = int(input())

def slope_check(array):
    pass

for t in range(1, T + 1):
    N, slope = map(int, input().split())
    tmp = []

    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 행
    for i in range(len(arr)):
        slope_check(arr[i])

    # 열
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            pass

    '''
    [2, 2, 3, 2, 2, 2]
    행 or 열 탐색을 할 때 그 중 제일 큰 값 구하고,
    앞 뒤로 있는 값이 큰 값의 길이 (ex 1) 보다 크고 slope보다 길이가 크거나 같은 경우 비탈길 가능?
    '''

    '''
    가로(행) 탐색, 세로(열)의 모든 케이스를 check_slope 함수에 넣어 가능하면 1, 불가능하면 0 리턴.
    slope_check () 함수에서

    같은 높이이면 cnt += 1
    높이 1 높아질 때, 그동안의 쌓아온 거리가 경사로(slope) 길이보다 크거나 같다면 가능한 경우이므로 cnt = 1로 초기화
    높이 1 낮아질 때, 현재 쌓아온 거리가 0보다는 크거나 같다면 현재 쌓아온 거리를 음수 값으로 땡겨주어 경사로 길이만큼 같은 높이를 유지할 때 경사로를 설치할 있도록 함. cnt = -X + 1
    높이 2 이상 차이나면 경사로 건설할 수 없는 경우이므로 리턴 0
    '''
