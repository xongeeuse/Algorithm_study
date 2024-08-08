import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 버스 노선 개수
    bus_route = []     # 각 버스가 다니는 정류장 범위 리스트

    for i in range(N):
        bus_route.append(list(map(int, input().split())))

    P = int(input())    # 버스 정류장 개수
    busstops = []         # ???
    for i in range(P):
        busstops.append(int(input()))

    result = [0] * P
    for i, j in bus_route:
        for k in range(len(busstops)):
            if i <= busstops[k] <= j:
                result[k] += 1

    print(f'#{tc}', *result)