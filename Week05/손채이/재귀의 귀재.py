def recursion(s, l, r):
    global cnt  # 재귀호출 횟수 저장할 전역 변수
    cnt += 1    # 호출 될 때마다 + 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for t in range(T):
    text = input()
    cnt = 0

    # 팰린드롬 T / F, cnt
    print(isPalindrome(text), cnt)
