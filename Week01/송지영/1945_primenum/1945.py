import sys
sys.stdin = open('input.txt')

T = int(input())
nums = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
    N = int(input())
    result = []
    for num in nums:
        cnt = 0
        while True:
            if N % num == 0:
                N //= num
                cnt += 1
            else:
                result.append(cnt)
                break
    print(f'#{tc}', *result)
