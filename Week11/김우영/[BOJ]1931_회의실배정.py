N = int(input())

meet_time = []
end = 0 # 범위 0 ~ 2^31 - 1 이기 때문에 비교 최소값으로 0지정
count = 0

for _ in range(N):
    start_time, end_time = map(int, input().split())
    meet_time.append([end_time, start_time]) # 끝나는 시간 기준으로 정렬하려고 end, start로 넣음
meet_time.sort() # 끝나는 시간이 짧은 순대로 오름차순 정렬

for new_end, new_start in meet_time:
    if end <= new_start:
        count += 1
        end = new_end
print(count)