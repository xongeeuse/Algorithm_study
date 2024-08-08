import sys

sys.stdin = open('9490_input.txt')

T = int(input())

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cnt = arr[i][j]
            for k in range(len(dxy)):
                for x in range(1, arr[i][j] + 1):
                    point_x = i + dxy[k][0] * x
                    point_y = j + dxy[k][1] * x

                    if 0 <= point_x < len(arr) and 0 <= point_y < len(arr[0]):
                        cnt += arr[point_x][point_y]
            if max_value < cnt:
                max_value = cnt
    print(f'#{t} {max_value}')