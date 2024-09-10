import sys
sys.stdin = open("input.txt", "r")


def dfs(idx, c_v, p, m, mul, div):  # 인덱스, 현재 값, +, -, *, /
    global max_result, min_result

    # 종료 조건
    if idx == N:
        max_result = max(max_result, c_v)
        min_result = min(min_result, c_v)
        return

    # 덧셈 연산자 사용 가능한 경우
    if p > 0:
        dfs(idx + 1, c_v + numbers[idx], p - 1, m, mul, div)

    if m > 0:
        dfs(idx + 1, c_v - numbers[idx], p, m - 1, mul, div)

    if mul > 0:
        dfs(idx + 1, c_v * numbers[idx], p, m, mul - 1, div)

    # 나눗셈 연산자 사용 가능한 경우
    if div > 0:
        # 음수일 때 주의해야함
        if c_v < 0:
            dfs(idx + 1, -(-c_v // numbers[idx]), p, m, mul, div - 1)
        else:
            dfs(idx + 1, c_v // numbers[idx], p, m, mul, div - 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))  # 각 연산자의 개수('+', '-', '*', '/')
    numbers = list(map(int, input().split()))   # 수식에 사용되는 숫자

    max_result = float('-inf')
    min_result = float('inf')

    dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

    print(f'#{tc}', max_result - min_result)





