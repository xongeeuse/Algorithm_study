T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 움직일 값 설정 (작은 걸 움직일 것임)
    move = N
    fix = M
    if move > M:
        move, fix = M, N

    # 한 범위의 인덱스의 곱의 합을 담을 리스트
    sum_list = []
    
    if N < M:
        for i in range(fix-move+1):
            # 각 인덱스의 곱의 합을 담을 변수
            temp_sum = 0
            for j in range(move):
                temp_sum += A[j] * B[i+j]
            sum_list.append(temp_sum)
        ans = max(sum_list)
    else:
        for i in range(fix-move+1):
            temp_sum = 0
            for j in range(move):
                temp_sum += B[j] * A[i+j]
            sum_list.append(temp_sum)
        ans = max(sum_list)
    
    print(f'#{tc} {ans}')