def hanoi(n, first, third, second):
    if n == 1:
        print(f"{first} {third}")
        return
    hanoi(n - 1, first, second, third)  # 1단계: n-1개의 원판을 시작점에서 보조 기둥으로 이동
    print(f"{first} {third}")      # 2단계: 가장 큰 원판을 목표 기둥으로 이동
    hanoi(n - 1, second, third, first)  # 3단계: 보조 기둥에 있던 n-1개의 원판을 목표 기둥으로 이동


n = int(input())   # 원판 개수 입력
print(2**n - 1)    # 최소 이동 횟수 출력
hanoi(n, 1, 3, 2)  # 재귀적으로 이동 순서 출력
