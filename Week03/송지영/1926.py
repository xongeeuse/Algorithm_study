import sys
sys.stdin = open('input.txt')

N = int(input())
targets = '369'
result = [''] * N

for i in range(1, N+1):
    num = str(i)
    for j in range(len(num)):
        if num[j] not in targets:                           # j가 3, 6, 9 아닐 때
            if '-' in result[i-1]:                          # 결과에 -가 있으면 패스
                continue
            result[i-1] += num[j]                           # 없으면 결과값에 숫자 넣어라

        if num[j] in targets:                               # j가 3, 6, 9 일 때
            if result[i-1].isdecimal():                     # 결과값에 이미 숫자가 들어 있으면
                result[i-1] = '-'                           # 박수로 재할당
            else:                                           # 숫자 아니면
                result[i-1] += '-'                          # 박수 추가

print(*result)