def make_tree(node):
    global num
    if node <= (2 ** K) - 1:
        make_tree(node * 2)
        tree[node] = arr[num]
        num += 1
        make_tree(node * 2 + 1)

K = int(input()) # 트리의 높이 - 1
arr = list(map(int, input().split()))
tree = [0] * ((2 ** K)) # 원소의 최대 개수는 2**K-1이므로 인덱스 번호와 맞추기 위해.
num = 0 # arr의 인덱스의 접근할 변수
make_tree(1) # 문제 조건을 만족하며 arr를 기준으로 한 tree가 만들어짐

# 출력
for i in range(K):
    for j in range(2**i):
        print(tree[2**i + j], end = " ")
    print()