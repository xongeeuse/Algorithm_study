T = int(input())

def pascal_triangle(i, j):
    if i == j or j == 0:
        return 1
    return pascal_triangle(i - 1, j - 1) + pascal_triangle(i - 1, j)

for t in range(1, 1 + T):
    N = int(input())
    triangle = []

    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(pascal_triangle(i, j))
        triangle.append(row)

    # for i in range(2, len(triangle)):
    #     for j in range(1, len(triangle[i]) - 1):
    #         if 0 <= i < len(triangle) and 0 <= j < len(triangle[i]):
    #             triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    print(f'#{t}')

    for i in range(len(triangle)):
        print(*triangle[i])