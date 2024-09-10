import sys
sys.stdin = open("input.txt", "r")


arr = [i for i in range(1, 13)]
path = []


def subset_sum(p):  # 부분집합
    global temp_sum, cnt
    temp_sum = sum(p)
    if temp_sum == K:
        cnt += 1


def subset(lev, start):
    if lev == N:
        subset_sum(path)
        return

    for i in range(start, 12):
        path.append(arr[i])
        subset(lev+1, i+1)
        path.pop()


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 부분집합 원소의 수 : N, 집합의 합 : K
    temp_sum = 0
    cnt = 0
    subset(0, 0)
    print(f'#{tc}', cnt)

