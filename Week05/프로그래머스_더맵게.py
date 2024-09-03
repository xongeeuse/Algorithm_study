# EOF 에러
def solution(scoville, K):
    mix_cnt = 0
    while scoville[0] < K:  # 제일 앞에 스코빌이 기준 지수보다 작을 때만
        scoville.sort()  # 스코빌 지수 작은거부터 정렬
        mix_scoville = scoville[0] + scoville[1] * 2
        mix_cnt += 1
        scoville = scoville[2:]
        scoville.append(mix_scoville)
    answer = mix_cnt
    return answer

scoville = list(map(int, input().split())) # [1, 2, 3, 9, 10, 12]
K = int(input()) # 7

print(solution(scoville, K))