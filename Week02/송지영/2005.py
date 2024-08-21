import sys
sys.stdin = open('input.txt')


def pascal(N):
    data = [[0] * i for i in range(1, N+1)]         # 0으로 채워진 프레임 만들기
    for i in range(N):                              # 각 행의 양 끝 값 1 할당
        data[i][0] = 1
        data[i][-1] = 1

    # for i in range(N):                                    # 반복문 합쳐도 작동하네?
        for j in range(i+1):
            if data[i][j] != 1:                             # 현재 위치의 값이 1이 아닐 때
                data[i][j] = data[i-1][j-1] + data[i-1][j]  # 왼쪽과 오른쪽 위의 숫자의 합 배정

    return data


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for p in pascal(N):
        print(*p)
