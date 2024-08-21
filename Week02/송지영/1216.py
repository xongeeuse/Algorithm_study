import sys
sys.stdin = open('input.txt', "r")

def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def find_palindrome(data):
    for i in range(N):
        for length in range(N, 1, -1):
            for start in range(N - length + 1):
                if is_palindrome(data[i][start:start+length]):
                    return length

                column = []
                for j in range(start, start + length):
                    column.append(data[j][i])

                if is_palindrome(column):
                    return length
    return 1



T = 10
for _ in range(1, T+1):
    tc = int(input())
    N = 100
    data = [input() for _ in range(N)]
    result = find_palindrome(data)

    print(f'#{tc} {result}')
