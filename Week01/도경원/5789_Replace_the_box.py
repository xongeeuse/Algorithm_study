# T = int(input())
# for tc in range(1, T+1):
#     n, q = map(int, input().split())
#     a = [0] * n
#     for qq in range(q):
#         i1, i2 = map(int, input().split())
#         for i in range(i1-1, i2):
#             a[i] = i1
#     print(f'#{tc}', *a)

T = int(input())
for tc in range(1, T + 1):
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(1, q+1): # qq에 0과 1이 들어감
        i1, i2 = map(int, input().split())
        for j in range(i1 - 1, i2): # 인덱스 번호이기 때문에.
            a[j] = i
    print(f'#{tc}', *a)