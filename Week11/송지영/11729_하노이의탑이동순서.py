def move(N, start, to):
    # print(f'{N}번 원반을 {start}에서 {to}로 이동')
    print(start, to)

def hanoi(N, start, to, via):   # to: 목적 기둥
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N - 1, start, via, to)
        move(N, start, to)
        hanoi(N - 1, via, to, start)

N = int(input())    # N: 원판의 개수
K = 2 ** N - 1      # K: 옮긴 횟수

print(K)
hanoi(N, 1, 3, 2)   # 3번 기둥이 목적 기둥이랏거!
