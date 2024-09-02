# import sys
# sys.stdin = open('input.txt')
'''
0
1
3
2
'''

def cantor_set(length):
    global data
    if N == 0:
        return

    while length > 1:
        length //= 3
        for idx in range(length, length * 2):
            data[idx] = ' '
    return


T = 4
for tc in range(1, T + 1):
    N = int(input())
    data = list('-' * 3 ** N)
    cantor_set(length=3**N)
    print(''.join(data))
