def binary_tree(lst, d):
    # 현재 트리의 루트 인덱스
    # arr의 가운데 값
    # depth = 0에 올 값
    # ex) 3
    #   6    2
    # 1  4  5   7
    root = len(lst) // 2

    # result의 depth에 lst[root] = 3 할당
    result[d].append(lst[root])

    # 리스트에 노드가 하나만 있으면 트리 못 만드니까 종료
    if len(lst) == 1:
        return

    # 루트의 왼쪽 서브트리
    binary_tree(lst[:root], d + 1)
    # 루트의 오른쪽 서브트리
    binary_tree(lst[root + 1:], d + 1)

K = int(input())        # 트리 깊이
arr = list(map(int, input().split()))       # 방문 순서(중위순회)
result = [[] for _ in range(K)]     # K 깊이의 트리 형태 저장

# 트리 만드는 함수 arr를 가지고 만들어야함. 처음 깊이는 0부터
binary_tree(arr, 0)

for i in range(len(result)):
    print(*result[i])