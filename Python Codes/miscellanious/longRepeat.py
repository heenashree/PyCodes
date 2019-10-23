def long_repeat(line: str) -> int:
    ans, temp = 1, 1
    if len(line) == 0:
        return 0

    # Traverse the string
    for i in range(1, len(line)):

        # If character is same as
        # previous increment temp value
        if (line[i] == line[i - 1]):
            temp += 1
        else:
            ans = max(ans, temp)

            temp = 1

    ans = max(ans, temp)
    return ans


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')