import sys
sys.stdin = open('input.txt')

def cal(n1, n2, oper_idx):
    if oper_idx == 0:
        return n1 + n2

    if oper_idx == 1:
        return n1 - n2

    if oper_idx == 2:
        return n1 * n2

    if oper_idx == 3:
        if n1 < 0:
            return -(abs(n1) // n2)
        return n1 // n2

def dfs(level, total):
    global mn, mx

    if level == N:
        mn = min(mn, total)
        mx = max(mx, total)
        return

    for i in range(4):
        if opers[i] == 0:
            continue

        opers[i] -= 1
        dfs(level + 1, cal(total, nums[level], i))
        opers[i] += 1




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    mn, mx = float('inf'), float('-inf')

    dfs(1, nums[0])
    print(f'#{tc}', mx - mn)