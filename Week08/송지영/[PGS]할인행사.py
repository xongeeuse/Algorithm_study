def solution(want, number, discount):
    answer = 0

    shopping_list = []
    for i in range(len(want)):
        shopping_list += [want[i]] * number[i]

    shopping_list.sort()
    print(shopping_list)

    for i in range(len(discount) - 9):
        if shopping_list == sorted(discount[i:i + 10]):
            answer += 1

    return answer

# 출력
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork",
            "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))