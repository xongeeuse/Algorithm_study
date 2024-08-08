T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while True:
        if N % 2 == 0:
            a += 1
            N //= 2
        elif N % 3 == 0:
            b += 1
            N //= 3
        elif N % 5 == 0:
            c += 1
            N //= 5
        elif N % 7 == 0:
            d += 1
            N //= 7
        elif N % 11 == 0:
            e += 1
            N //= 11
        elif N == 1 or N % 2 != 0 and N % 3 != 0 and N % 5 != 0 and N % 7 != 0 and N % 11 != 0:
            break
    print(f'#{tc} {a} {b} {c} {d} {e}')