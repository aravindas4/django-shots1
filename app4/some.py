# String input: {}]}[])
# {

stack = []

mappings = {
    "}": "{",
    "]": "[",
    ")": "("
}


def is_valid(string):

    for char in string:

        if char in ["(", "{", "["]:
            stack.append(char)

        elif char in ["}", ")", "]"]:
            if len(stack) < 1 or stack[-1] != mappings[char]:
                return False
            else:
                stack.pop()

    return stack == []


# INput: number
# Output: just smaller prime number whcih is a palindrome
# 121, 2332

import math


def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]


def get_prime(input_num):
    # square_root = cmath.sqrt(input_num)

    for num in range(input_num, 1, -1):
        square_root = int(math.sqrt(num))
        # print(f"{num} -> {square_root}")

        for factor in range(square_root, 2, -1):
            if num % factor == 0:
                break
        else:
            if is_palindrome(num):
                return num

    return -1


if __name__ == '__main__':
    print("Plz input a num")
    # inp = input().strip()
    # print(is_valid(inp))
    # # [[]][{{{}}}}
    num = int(input().strip())
    print(get_prime(num))
