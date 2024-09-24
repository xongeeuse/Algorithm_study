from collections import Counter


def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))

    for i in range(len(discount) - 9):
        window = discount[i:i + 10]
        window_counter = Counter(window)

        if all(window_counter[item] == want_dict[item] for item in want):
            answer += 1

    return answer