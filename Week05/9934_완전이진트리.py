def make_tree(node):
    global num
    if node <= (2 ** K) - 1: # 트리의 범위 안에 있을 때
        make_tree(node * 2) # 왼쪽이 있으면 왼쪽으로 들어가라
        tree[node] = arr[num] # 왼쪽 못들어가면 지금 위치에 숫자 넣고
        num += 1 # 숫자 더해줌
        make_tree(node * 2 + 1) # 오른쪽 있으면 오른쪽으로 들어가라

K = int(input()) # 트리의 높이 - 1
arr = [0] + list(map(int, input().split())) # 인덱스 번호와 num 맞추기 위해 제로패딩
tree = [0] * ((2 ** K)) # 원소의 최대 개수는 2**K-1이므로 인덱스 번호와 맞추기 위해.
num = 1 # arr의 인덱스의 접근할 변수
make_tree(1) # 문제 조건을 만족하며 arr를 기준으로 한 tree가 만들어짐

# 출력
for i in range(K):
    for j in range(2**i):
        print(tree[2**i + j], end = " ")
    print()