# 팩토리얼을 계산하는 함수 정의
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 조합 계산 함수
def combination(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))


# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    # 조합 계산 (M개 중에 N개를 선택하는 경우의 수)
    print(combination(m, n))
