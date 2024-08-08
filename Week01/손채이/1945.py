import sys

sys.stdin = open('1945_input.txt')

T = int(input())

for tc in range(1, T + 1):
    num_dict = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0
    }

    N = int(input())

    for i in num_dict.keys():
        while N != 1:
            if N % i == 0:
                num_dict[i] += 1
                N //= i
            else:
                break

    print(f'#{tc}', *num_dict.values())