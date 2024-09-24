def solution(input_string):
    answer = ''

    result = []
    for char in input_string:
        if not result:
            result.append(char)
            continue

        if char == result[-1]:
            continue
        result.append(char)

    result.sort()

    for r in result:
        if r not in answer and result.count(r) > 1:
            answer += r

    if not answer:
        return 'N'

    return answer


# 출력
input_strings = ["edeaaabbccd",
                 "eeddee",
                 "string",
                 "zbzbz"]

for input_string in input_strings:
    print(solution(input_string))

