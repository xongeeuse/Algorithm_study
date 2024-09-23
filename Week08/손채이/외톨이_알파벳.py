# Python 풀이 : Crush on Study
def solution(input_string):
    lonely_alphabets = set()
    current_char = ''
    string = set()

    for char in input_string:
        if char != current_char:
            if char in string:
                lonely_alphabets.add(char)
            string.add(char)
            current_char = char

    if lonely_alphabets:
        return ''.join(sorted(lonely_alphabets))
    else:
        return "N"
