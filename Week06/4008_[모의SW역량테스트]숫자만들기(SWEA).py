# # sol_1 - 온라인 강사님 풀이
#
# def cal(num1, num2, oper_idx):
#     if oper_idx == 0:
#         return num1 + num2
#     if oper_idx == 1:
#         return num1 - num2
#     if oper_idx == 2:
#         return num1 * num2
#     if oper_idx == 3:
#         if num1 < 0: # 음수처리
#             return -(abs(num1) // num2)
#         return num1 // num2
#
#
# # 재귀 설계
# # 시작점: 첫 번째 숫자부터
# # 끝점: 모든 수(연산자)를 사용할 때 까지
# # 파라미터: level: 숫자의 번호, total: 특정 시점에서 계산된 결과값
#
# def my_dfs(level, total):
#     global min_result, max_result
#
#     if level == N:
#         min_result = min(min_result, total)
#         max_result = max(max_result, total)
#         return
#
#     # 4개의 연산자를 확인
#     for i in range(4):
#         if opers[i] == 0: # 남은 연산자가 없다면 넘기기
#             continue
#
#         opers[i] -= 1 # 연산자를 사용했기에 빼기
#         my_dfs(level + 1, cal(total, numbers[level], i))
#         opers[i] += 1 # 다음 호출에서는 다시 사용하기 위해 다시 더해주기
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     opers = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#     min_result = 1e9
#     max_result = -1e9
#
#     my_dfs(1, numbers[0])
#     print(f'#{tc} {max_result - min_result}')


# sol_2 - 지웅이형
def my_dfs(n):
    # 종료 조건
    global cal

    if n == N - 1:
        ans.append(cal)
        return

    for i in range(4):
        if opers[i] == 0:  # 연산할 수 없는 경우 다음 연산자로 넘김
            continue
        cal2 = cal # 초기값(계산전 값) 복사
        opers[i] -= 1

        if i == 0:
            cal += nums[n + 1]
        elif i == 1:
            cal -= nums[n + 1]
        elif i == 2:
            cal *= nums[n + 1]
        else:
            cal = int(cal / nums[n + 1])
        my_dfs(n + 1)
        opers[i] += 1
        cal = cal2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cal = nums[0]  # 처음 값 넣고 시작
    ans = []
    my_dfs(0)
    print(ans)
    print(f'#{tc} {max(ans) - min(ans)}')
