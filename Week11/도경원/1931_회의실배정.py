# 회의 개수 입력
n = int(input())

# 각 회의의 시작 시간과 종료 시간을 리스트로 입력받음
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

# 정렬 기준 함수
def meeting_key(meeting):
    return (meeting[1], meeting[0])  # 종료 시간, 시작 시간을 기준으로 반환

# sort 메서드를 사용하여 정렬 (정렬 기준 함수 사용)
meetings.sort(key=meeting_key)

# 그리디 알고리즘을 사용해 가능한 회의의 최대 개수를 구함
count = 0
end_time = 0

for meeting in meetings:
    start = meeting[0]
    end = meeting[1]
    if start >= end_time:  # 현재 회의의 시작 시간이 이전 회의의 종료 시간 이후일 때
        end_time = end     # 종료 시간을 현재 회의의 종료 시간으로 갱신
        count += 1         # 회의 개수 증가

# 결과 출력
print(count)
