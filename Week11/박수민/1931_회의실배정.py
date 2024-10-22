# 1931 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
# 회의 끝나는 시간 기준으로 정렬 후 
# 시작 시간 기준으로 정렬(x[1],x[0])
# 회의가 일찍 끝날 수록 쓸 수 있는 시간이 많아지니까
conference = sorted(conf, key=lambda x:(x[1],x[0]))
a = 0
comp = 1
while True:
    # 끝까지 찾았으면 break
    if a + comp == N:
        break
    # 회의 끝난 시간, 다음 회의 시작 시간 비교
    # 끝난 시간 후에 시작하는 회의 찾으면 회의 개수(cnt) 하나 더해주고
    # 시작점 재설정, 비교하는 comp도 1로 초기화
    if conference[a][1] <= conference[a+comp][0]:
        cnt += 1
        a = a+comp
        comp = 1        
    else:
        comp += 1

print(cnt)