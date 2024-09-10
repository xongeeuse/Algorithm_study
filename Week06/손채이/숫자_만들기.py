# 사칙연산 계산 함수
# num1과 num2를 oper_idx에 해당하는 연산을 사용해 계산함
def cal(num1, num2, oper_idx):
    if oper_idx == 0:  # oper_idx가 0이면 덧셈
        return num1 + num2
    if oper_idx == 1:  # oper_idx가 1이면 뺄셈
        return num1 - num2
    if oper_idx == 2:  # oper_idx가 2이면 곱셈
        return num1 * num2
    if oper_idx == 3:  # oper_idx가 3이면 나눗셈
        # 음수를 양수로 나눈 후 다시 음수로 만드는 경우
        if num1 < 0:
            return -(abs(num1) // num2)
        return num1 // num2  # 양수끼리 나눗셈은 기본 정수 나눗셈

# 깊이 우선 탐색 (DFS) 함수
# level: 현재 진행된 연산의 단계
# total: 지금까지 계산된 값
def dfs(level, total):
    global min_result, max_result  # 최솟값과 최댓값을 전역 변수로 사용

    # 모든 숫자를 다 사용했으면 (즉, level이 N이면) 결과값을 갱신
    if level == N:
        min_result = min(min_result, total)  # 최소값 갱신
        max_result = max(max_result, total)  # 최대값 갱신
        return  # 재귀 종료

    # 4가지 연산자에 대해 반복 (덧셈, 뺄셈, 곱셈, 나눗셈 순서)
    for i in range(4):
        if opers[i] == 0:  # 사용 가능한 연산자가 없으면 건너뜀
            continue

        opers[i] -= 1  # 연산자를 하나 사용
        # 다음 레벨로 재귀적으로 탐색, numbers[level]을 계산에 포함
        dfs(level + 1, cal(total, numbers[level], i))
        opers[i] += 1  # 재귀가 끝나면 연산자를 다시 복구 (원상태로)

# 입력 처리 부분
T = int(input())  # 테스트 케이스 수 입력

for t in range(1, T + 1):
    N = int(input())  # 사용할 숫자의 개수
    opers = list(map(int, input().split()))  # 연산자의 개수 (덧셈, 뺄셈, 곱셈, 나눗셈 순)
    numbers = list(map(int, input().split()))  # 사용할 숫자 리스트

    min_result = 1e9  # 최소 결과값을 큰 수로 초기화
    max_result = -1e9  # 최대 결과값을 작은 수로 초기화

    # dfs 탐색 시작, 첫 번째 숫자는 계산 결과로 사용하므로 dfs는 level 1부터 시작
    dfs(1, numbers[0])

    # 최종 결과 출력, 최대값과 최소값의 차이를 출력
    print(f'#{t} {max_result - min_result}')
