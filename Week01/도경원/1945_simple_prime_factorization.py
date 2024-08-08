import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    a, b, c, d, e = 0, 0, 0, 0, 0
    N = int(input())
    while True:
        if N % 11 == 0:
            N //= 11
            e += 1
        elif N % 7 == 0:
            N //= 7
            d += 1
        elif N % 5 == 0:
            N //= 5
            c += 1
        elif N % 3 == 0:
            N //= 3
            b += 1
        elif N % 2 == 0:
            N //= 2
            a += 1
        else:
            break
    print(f'#{tc} {a} {b} {c} {d} {e}')


