# M개 중 N개 뽑는 조합

def fac(n):
    temp_num = 1
    for i in range(1, n+1):
        temp_num *= i
    return temp_num

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    print(fac(M) // (fac(N) * fac(M-N)))