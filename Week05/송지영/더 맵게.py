import sys
sys.stdin = open('input.txt')

'''
heapq.heappush(heap, i) heap에 i 추가
heapq.heappop(heap) 가장 작은 원소 삭제 후 값 리턴
heapq.heapify(heap) 기존 리스트 힙으로 변환
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)             # scoville 리스트 => heap으로 변환
    answer = 0                          # 횟수 받아줄 변수 생성

    while scoville:
        if scoville[0] >= K:            # 가장 덜 매운 음식의 스코빌 지수가 이미 K 이상이면
            return answer               # 횟수 리턴

        if len(scoville) < 2:           # 섞을 음식이 2개 미만으로 남았다면 -1 리턴
            return -1

        i1 = heapq.heappop(scoville)    # 가장 덜 매운 음식과
        i2 = heapq.heappop(scoville)    # 두번째로 덜 매운 음식 pop

        heapq.heappush(scoville, i1 + (i2 * 2))     # 섞어서 다시 scoville에 넣어주고
        answer += 1                                 # 횟수 + 1

    return -1

scoville = list(map(int, input().split()))
K = int(input())
print(solution(scoville, K))

