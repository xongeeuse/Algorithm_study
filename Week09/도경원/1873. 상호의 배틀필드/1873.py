# 상하좌우 방향 정의 (U, D, L, R)
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
tank_symbols = {'U': '^', 'D': 'v', 'L': '<', 'R': '>'}


def move_tank(H, W, grid, commands, tank_x, tank_y, tank_dir):
    for command in commands:
        if command == 'S':  # Shoot
            bullet_x, bullet_y = tank_x, tank_y
            dx, dy = directions[tank_dir]

            # 총알이 나아가는 방향으로 진행
            while True:
                bullet_x += dx
                bullet_y += dy
                if not (0 <= bullet_x < H and 0 <= bullet_y < W):
                    break  # 맵을 벗어남
                if grid[bullet_x][bullet_y] == '*':  # 벽돌벽에 맞음
                    grid[bullet_x][bullet_y] = '.'  # 벽을 부숨
                    break
                if grid[bullet_x][bullet_y] == '#':  # 강철벽에 맞음
                    break  # 아무일도 일어나지 않음
        else:
            # 전차 방향 전환
            tank_dir = command
            grid[tank_x][tank_y] = tank_symbols[tank_dir]
            dx, dy = directions[tank_dir]

            # 전차가 이동할 수 있는지 확인
            new_x, new_y = tank_x + dx, tank_y + dy
            if 0 <= new_x < H and 0 <= new_y < W and grid[new_x][new_y] == '.':
                # 전차 이동
                grid[tank_x][tank_y] = '.'  # 이전 위치는 평지로
                tank_x, tank_y = new_x, new_y  # 전차 위치 갱신
                grid[tank_x][tank_y] = tank_symbols[tank_dir]  # 새 위치에 전차 표시

    return grid


def find_tank(H, W, grid):
    # 전차의 위치와 방향을 찾기
    for i in range(H):
        for j in range(W):
            if grid[i][j] in tank_symbols.values():
                for direction, symbol in tank_symbols.items():
                    if grid[i][j] == symbol:
                        return i, j, direction
    return -1, -1, ''  # 전차를 찾지 못한 경우


def battlefield():
    T = int(input())  # 테스트 케이스 개수
    for _ in range(T):
        H, W = map(int, input().split())  # 맵의 크기
        grid = [list(input().strip()) for _ in range(H)]  # 맵 정보
        N = int(input())  # 명령어 개수
        commands = input().strip()  # 명령어 목록

        # 전차 위치와 방향 찾기
        tank_x, tank_y, tank_dir = find_tank(H, W, grid)

        # 명령어 처리
        grid = move_tank(H, W, grid, commands, tank_x, tank_y, tank_dir)

        # 결과 출력
        for row in grid:
            print(''.join(row))

# 실행
battlefield()
