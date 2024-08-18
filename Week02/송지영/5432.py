import sys
sys.stdin = open('input.txt')

def count_pipes(data):
    stack = []
    opened = '('
    closed = ')'

    # 레이저 찾아서 0으로 바꾸기
    for d in data:
        if d == closed and stack[-1] == opened:
            stack.pop()
            stack.append('0')
        else:
            stack.append(d)

    cnt = 0         # open 막대기 누적 카운트
    result = 0      # 잘린 막대 개수 총 합
    for s in stack:
        if s == opened:
            cnt += 1
        elif s == '0':
            result += cnt
        elif s == closed:
            cnt -= 1
            result += 1
    return result


T = int(input())

for tc in range(1, T+1):
    data = input()

    print(f'#{tc}', count_pipes(data))