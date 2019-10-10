def count_consecutive_summers(num):
    #Formula = (N - L(L+1)/2)/L+1 so N > L(L+1)/2
    L = 1
    count = 0
    while  L(L+1)/2 < num:


    return None


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
