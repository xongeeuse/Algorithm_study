import sys
sys.stdin = open('input.txt')
'''
5
AAA
ABBA
ABABA
ABCA
PALINDROME
'''

def recursion(s, l, r):
    global cnt
    cnt += 1        # 재귀함수 호출 횟수 카운트
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else: return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for tc in range(1, T+1):
    data = input()
    cnt = 0
    print(isPalindrome(data), cnt)
