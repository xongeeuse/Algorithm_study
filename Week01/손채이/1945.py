import sys

sys.stdin = open('1945_input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 각 숫자의 횟수를 세기 위해 숫자를 키로 가진 딕셔너리 생성
    num_dict = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0
    }

    N = int(input())
    # 딕셔너리의 키 값만큼 반복을 함
    for i in num_dict.keys():
        # 입력 받은 숫자가 1 되기 전까지 반복함
        while N != 1:
            # N을 딕셔너리의 키 값(i)으로 나눈 나머지가 0일 경우 num_dict의 키 값 i의 value에 +1
            # 다음을 위해 N을 i로 나눈 값으로 재할당
            if N % i == 0:
                num_dict[i] += 1
                N //= i
            else:
                break

    print(f'#{tc}', *num_dict.values())