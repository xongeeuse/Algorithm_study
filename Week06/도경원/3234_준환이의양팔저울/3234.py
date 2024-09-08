def dfs(idx, left, right):
    global count

    # 왼쪽 저울이 오른쪽 저울보다 가벼워지면 그만 둔다 (백트래킹)
    if left < right:
        return

    # 모든 추를 다 배치했다면 카운트 증가
    if idx == N:
        count += 1
        return

    # 다음 추를 왼쪽에 올리기
    dfs(idx + 1, left + weights[idx], right)

    # 다음 추를 오른쪽에 올리기
    dfs(idx + 1, left, right + weights[idx])


def solve(weights):
    global count
    count = 0
    # 추들의 모든 순열을 순차적으로 확인
    perm(weights, 0)
    return count


# 순열 생성 함수
def perm(arr, k):
    if k == len(arr):
        dfs(0, 0, 0)
    else:
        for i in range(k, len(arr)):
            arr[k], arr[i] = arr[i], arr[k]
            perm(arr, k + 1)
            arr[k], arr[i] = arr[i], arr[k]


# 테스트케이스 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    count = 0
    result = solve(weights)
    print(f'#{tc} {result}')
