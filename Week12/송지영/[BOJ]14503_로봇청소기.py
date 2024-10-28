import sys
sys.stdin = open('input.txt')

# 틀림ㅠ

'''
시작칸 (r, c) 방문 처리 => 근데 2로 원본 data에 처리하면 안되나? 
0 청소 안함 1 벽 2 청소 완

상우하좌 순서로 델타 탐색
근데 처음 바라보고 있던 방향에 따라 델타 탐색 순서 달라지는데 어떻게 적용?
일단 하드코딩해 + 돌았을 때 방향도 넣어버림ㅠ
1) d=0 : [[0, -1], [-1, 0], [0, 1], [1, 0]]
2) d=1 : [[1, 0], [0, -1], [-1, 0], [0, 1]]
3) d=2 : [[0, 1], [1, 0], [0, -1], [-1, 0]]
4) d=3 : [[-1, 0], [0, 1], [1, 0], [0, -1]]

OMG (d + 3) % 4 를 활용해보세요?
'''
delta = [[[0, -1, 3], [-1, 0, 2], [0, 1, 1], [1, 0, 0]],
         [[1, 0, 0], [0, -1, 3], [-1, 0, 2], [0, 1, 1]],
         [[0, 1, 1], [1, 0, 0], [0, -1, 3], [-1, 0, 2]],
         [[-1, 0, 2], [0, 1, 1], [1, 0, 0], [0, -1, 3]]]

def robot(x, y, d):
    global result
    if not data[x][y]:          # 시작점 청소완 처리
        data[x][y] = 2
        result += 1

    dirty = 0
    for dx, dy, direction in delta[d]:
        nx, ny = x + dx, y + dy
        # if nx < 0 or nx >= N or ny < 0 or ny >= M:
        #     continue
        if data[nx][ny]:        # 벽이거나 청소완이면 넘어가고
            continue
        data[nx][ny] = 2
        result += 1
        nd = direction
        dirty = 1
        robot(nx, ny, nd)

    if dirty:
        return
    else:
        nx, ny = x + delta[d][1][0], y + delta[d][1][1]
        # if nx < 0 or nx >= N or ny < 0 or ny >= M:
        #     return
        if data[nx][ny] != 1:   # 벽만 아니면
            robot(nx, ny, d)    # 방향 유지한 채로 1칸 후진


N, M = map(int, input().split())
r, c, d = map(int, input().split())     # d: 0~3 북동남서 순서
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)
result = 0
robot(r, c, d)
# print(data)
print(result)
