import sys

sys.stdin = open('1961_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 회전한 배열을 저장하기 위한 리스트 만들기
    # 함수로 만들면 리스트 3개 안 만들었어도 됨. 리팩토링 필요함
    rotation_90 = [[0] * N for _ in range(N)]
    rotation_180 = [[0] * N for _ in range(N)]
    rotation_270 = [[0] * N for _ in range(N)]

    print(f'#{t}')
    '''
    1 2 3
    4 5 6
    7 8 9
    
    90도 회전
    7 4 1
    8 5 2
    9 6 3
    
    180도 회전
    9 8 7
    6 5 4
    3 2 1
    
    270도 회전
    3 6 9
    2 5 8
    1 4 7
    '''
    for i in range(N):
        for j in range(N):
            rotation_90[i][j] = arr[len(arr) - 1 - j][i]
            rotation_180[i][j] = arr[len(arr) - 1 - i][len(arr) - 1 - j]
            rotation_270[i][j] = arr[j][len(arr) - 1 - i]

        print(''.join(map(str, rotation_90[i])), end=' ')
        print(''.join(map(str, rotation_180[i])), end=' ')
        print(''.join(map(str, rotation_270[i])))

    # # 90도 회전
    # for i in range(N):
    #     for j in range(N - 1, -1, -1):
    #         print(arr[j][i], end='')
    #     print(' ')
    #
    # # 270도 회전
    # for i in range(N - 1, -1, -1):
    #     for j in range(N - 1, -1, -1):
    #         print(arr[i][j], end='')
    #     print(' ')
    #
    # for i in range(N - 1, -1, -1):
    #     for j in range(N):
    #         print(arr[j][i], end='')
    #     print(' ')
