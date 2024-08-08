T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    arr.append(0)
    num_one_list = []
    count_one = 0
    for i in range(N):
        if arr[i] == 1:
            count_one += 1
            if arr[i+1] == 1:
                continue
            else:
                num_one_list.append(count_one)
                count_one = 0

    print(f'#{tc} {max(num_one_list)}')
            

# 인터넷 풀이
# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     x = input().split('0')
#     max_x = 0
#     for i in x:
#         if max_x < len(i):
#             max_x = len(i)
#     print(f'#{tc} {max_x}')