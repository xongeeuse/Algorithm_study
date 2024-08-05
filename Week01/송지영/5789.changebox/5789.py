import sys
sys.stdin = open('input.txt')

T= int(input())

# SOL 1
# for tc in range(1, T+1):
#     N, Q = map(int, input().split())        # N : 상자의 개수, Q : 일정 범위의 연속한 상자를 동일한 숫자로 변경하는 횟수
#     LRs = [list(map(int, input().split())) for _ in range(Q)]
#     boxes = [0] * N
#
#     for i in range(1, len(LRs)+1):
#         L, R = LRs[i-1]
#         boxes[L-1:R] = [i] * (R - L + 1)
#
#     print(f'#{tc}', *boxes)


# another SOL
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        boxes[L-1:R] = [i] * (R-L+1)

    print(f'#{tc}', *boxes)