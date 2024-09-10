import sys
sys.stdin = open('input.txt')

'''
(Runtime error)
Error Message:
Memory Limit Exceeded
'''

import itertools
from collections import deque

def calculator():
    global mx, mn

    nums = deque(numbers)
    operators = deque(permu_oper)
    while operators:
        if len(nums) == N:
            n1 = nums.popleft()
        n2 = nums.popleft()
        oper = operators.popleft()

        if oper == '+':
            n1 = int(n1 + n2)
        elif oper == '-':
            n1 = int(n1 - n2)
        elif oper == '*':
            n1 = int(n1 * n2)
        elif oper == '/':
            n1 = int(n1 / n2)

    if mn > n1: mn = n1
    if mx < n1: mx = n1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator = ['+', '-', '*', '/']
    operators = list(map(int, input().split()))     # +, -, *, / 순서
    numbers = list(map(int, input().split()))
    mn, mx = float('inf'), float('-inf')

    opers = []
    for i in range(4):
        for j in range(operators[i]):
            opers.append(operator[i])

    # 주어진 연산자들로 순열 생성
    permu_operators = list(set(list(itertools.permutations(opers))))
    # print(permu_operators)

    # 만들어진 순열대로 반복문 돌리기
    for permu_oper in permu_operators:
        calculator()

    print(f'#{tc}', mx - mn)