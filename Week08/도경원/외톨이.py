def solution(input_string):
    lonely_alphabet = set()
    prev_char = ''

    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i - 1]:
            if prev_char == input_string[i - 1]:
                lonely_alphabet.add(prev_char)
            prev_char = input_string[i - 1]

    result = ''.join(sorted(lonely_alphabet))
    return result if result else "N"