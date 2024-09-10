import sys  # 표준 입력을 받기 위해 sys 모듈을 사용

# 테스트 케이스의 개수 입력받기
T = int(sys.stdin.readline().strip())

# 1부터 12까지의 숫자 리스트 생성
numbers = [i for i in range(1, 13)]  # numbers = [1, 2, 3, ..., 12]


# 부분집합을 탐색하는 재귀 함수
def recur(start, total, cnt):
    global result  # 결과 값을 전역 변수로 선언

    # 만약 cnt가 N과 같다면, 즉 N개의 원소를 선택했다면
    if cnt == N:
        # 선택한 원소들의 합이 K와 같으면
        if total == K:
            result += 1  # 경우의 수를 하나 증가시킴
        return  # 재귀 종료

    # 더 이상 선택할 원소가 없으면 종료
    if start >= len(numbers):
        return

    # 1. 현재 원소를 선택하지 않고 넘어가는 경우
    recur(start + 1, total, cnt)

    # 2. 현재 원소를 선택하는 경우 (numbers[start]를 더하고, cnt를 1 증가시킴)
    recur(start + 1, total + numbers[start], cnt + 1)


# 각 테스트 케이스마다 N과 K를 입력받아 처리
for t in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().strip().split())  # N: 선택할 원소 개수, K: 목표 합
    result = 0  # 결과 값을 저장할 변수 초기화
    recur(0, 0, 0)  # 재귀 함수 시작 (start=0, total=0, cnt=0부터 시작)

    # 각 테스트 케이스 결과 출력
    print(f'#{t}', result)
