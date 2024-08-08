import copy

def rotate_90(arr):
    matrix = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if i > j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for k in range(N):
        matrix[k] = matrix[k][::-1]
    
    return matrix

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    arr_90 = rotate_90(arr)
    arr_180 = rotate_90(arr_90)
    arr_270 = rotate_90(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, arr_90[i])), ''.join(map(str, arr_180[i])), ''.join(map(str, arr_270[i]))) 