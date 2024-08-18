import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    result = 0

    # data 성적 순으로 선택정렬
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if data[max_idx] < data[j]:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]

    for i in range(K):
        result += data[i]

    print(f'#{tc}', result)
