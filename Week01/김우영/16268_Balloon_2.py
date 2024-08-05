import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    temp_list = [] # 꽃가루의 합을 받을 리스트
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for _ in range(N):
        temp = [0] + list(map(int, input().split())) + [0]
        matrix.append(temp)
        arr = [[0] * (M+2)] + matrix + [[0] * (M+2)]
    
    for i in range(1, N+1): # 모든 행과
        for j in range(1, M+1): # 모든 열에 접근
            temp_sum = arr[i][j] # 네 방향의 합을 담을 변수
            # 제로 패딩 했으므로 1,1 에서 시작
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                temp_sum += arr[nx][ny]
            temp_list.append(temp_sum)
    
    max_v = temp_list[0]
    for x in temp_list:
        if max_v < x:
            max_v = x
    
    print(f'#{tc} {max_v}')


# # sol_2 - 방식은 똑같음
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 합을 담기 위한 리스트
#     sum_list = []
#     # 델타 검색하기 위한 좌표 리스트 (우, 하, 좌, 상)
#     dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#     # arr를 제로 패딩하며 입력 받음
#     arr = [[0] * (M+2)]
#     arr += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
#     arr += [[0] * (M+2)]


#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             # 각 방향의 합을 담기 위한 변수
#             temp_sum = arr[i][j]
#             for dx, dy in dxy:
#                 nx = i + dx
#                 ny = j + dy
#                 temp_sum += arr[nx][ny]
#             sum_list.append(temp_sum)            
            
#     ans = max(sum_list)

#     print(f'#{tc} {ans}')