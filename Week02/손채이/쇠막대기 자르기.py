T = int(input())

for t in range(1, T + 1):
    stick = input()
    stack = []
    result = 0

    for i in range(len(stick)):
        # 열린 괄호가 나오면 stack.append
        if stick[i] == '(':
            stack.append(stick[i])
        # 닫힌 괄호인 경우
        else:
            # 열린 괄호와 한 쌍이기 때문에 pop
            stack.pop()
            # 닫힌 괄호 직전의 원소가 열린 괄호면 레이저, 아니면 막대의 끝
            # 막대기는 레이저로 잘리고 += 1
            result += len(stack) if stick[i - 1] == '(' else 1

    print(f'#{t} {result}')