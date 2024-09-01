import heapq

def solution(scoville, K):
    heapq.heapify(scoville)     # 배열을 힙 구조로 재배열
    cnt = 0     # 횟수

    # 스코빌 값을 두 개 pop 해야 함 -> 조건으로 1 < len()
    # 스코빌의 0번째가 K보다 작아야 함 -> and [0] < K
    while 1 < len(scoville) and scoville[0] < K:
        # 앞에 두 값 pop
        s0 = heapq.heappop(scoville)
        s1 = heapq.heappop(scoville)
        # 문제 조건에 맞춰서 두번째 값에 * 2 한 값을 첫번째 값에 더하고 스코빌에 push
        # heappush = 이미 힙 구조를 가진 배열에 새로운 원소를 넣는 함수
        # 이 때 추가된 원소가 부모보다 작으면 자리 변경
        tmp = s0 + (s1 * 2)
        heapq.heappush(scoville, tmp)
        cnt += 1

    # 반복문이 끝나고 0번째 값이 K보다 작을 경우 -1
    if scoville[0] < K:
        return -1

    return cnt