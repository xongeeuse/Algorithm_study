def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_simple(string):
    return string == string[::-1]

def find_longest_palindrome(matrix):
    for i in range(N):
        for length in range(N, 1, -1):
            for start in range(N - length + 1):
                if is_palindrome(matrix[i][start:start + length]):
                    return length

                column = []
                for j in range(start, start + length):
                    column.append(matrix[j][i])

                if is_palindrome(column):
                    return length

    return 1

for _ in range(10):
    t = int(input())
    N = 100
    matrix = [input() for _ in range(N)]

    result = find_longest_palindrome(matrix)
    print(f"#{t} {result}")