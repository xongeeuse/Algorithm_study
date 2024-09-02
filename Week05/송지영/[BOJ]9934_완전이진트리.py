# import sys
# sys.stdin = open('input.txt')
'''
data = 완전이진트리를 중위순회한 결과
'''

# 중위 순회
def inorder(node):
    global tree_inorder
    left = node * 2             # 왼쪽 자식 노드 번호
    right = node * 2 + 1        # 오른쪽 자식 노드 번호

    if left <= N:               # 왼쪽 자식 있으면
        inorder(left)           # 왼쪽 순회 진행
    tree_inorder.append(node)   # 현 위치 방문하고
    if right <= N:              # 오른쪽 자식 있으면
        inorder(right)          # 오른쪽 순회 진행


K = int(input())                                    # K: 완전이진트리의 깊이
data = list(map(int, input().split()))              # 완전이진트리를 중위순회한 결과
N = 2**K - 1                                        # N: 노드의 총 개수

tree = list(range(N + 1))                   # 인덱스 참조 위해 완전이진트리 만들고
tree_inorder = [0]                          # 노드 번호 인덱스 활용 위해 [0] 초기 세팅
inorder(1)                                  # 중위순회하기

real_map = [0] * (N + 1)                    # 진짜 도시의 지도 받아줄 리스트 생성
for i in range(1, N + 1):
    real_map[tree_inorder[i]] = data[i - 1] # 중위순회결과의 인덱스대로 real_map에 넣어주기

for i in range(K):                          # 트리의 깊이만큼 반복
    for k in range(2**i):                   # 해당 레벨의 노드 개수만큼 반복
        print(real_map[2**i + k], end=' ')
    print()


    # print(data)