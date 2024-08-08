import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    temp = []
    ans_90 = []
    ans_180 = []
    ans_270 = []
    # 90도
    for j in range(n):
        for i in range(n-1, -1, -1):
            temp += [str(a[i][j])]  # str(문자열)로 변환해서 넣어야 함
        # ans_90.append("".join(temp))
        ans_90 += ["".join(temp)]  # 구분자 없이(""는 빈 문자열이므로) 새 리스트에 temp 값을 집어 넣음
        temp = []
    # print(ans_90)
    # 180도
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            temp += [str(a[i][j])]
        ans_180 += ["".join(temp)]
        temp = []
    # print(ans_180)
    # 270도
    for j in range(n-1, -1, -1):
        for i in range(n):
            temp += [str(a[i][j])]
        ans_270 += ["".join(temp)]
        temp = []
    # print(ans_270)
    print(f'#{tc}')
    for i in range(n):
        print(ans_90[i], ans_180[i], ans_270[i])


