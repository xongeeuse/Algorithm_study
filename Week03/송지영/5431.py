import sys
sys.stdin = open('input.txt')

def homework_check(data):
    result = []
    for i in range(1, N+1):
        if i not in data:
            result.append(i)
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N : 수강생 수, M : 과제 제출한 사람의 수
    data = list(map(int, input().split()))

    print(f'#{tc}', *homework_check(data))