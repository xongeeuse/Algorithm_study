import sys
sys.stdin = open('input.txt')

T = int(input())                                                # 테스트 케이스 입력

for testcase in range(1, T+1):
    N, M = (map(int, input().split()))                          # N x N 배열, M x M 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]   # 파리 N x N 배열로 받아오기

    max_kill = 0                                                # 잡을 수 있는 파리의 최댓값 변수 생성

    for i in range(N-M+1):                                      # 배열 넘어가지 않도록 범위 설정
        for j in range(N-M+1):
            kill = 0                                            # 해당 윈도우에서 잡는 파리 수 변수 생성
            for k in range(M):                                  # 파리채 크기만큼 반복
                for l in range(M):
                    kill += arr[i + k][j + l]
            if max_kill < kill:                                 # 최댓값보다 크면 재할당
                max_kill = kill

    print(f'#{testcase} {max_kill}')
