def checkio(first, second):
    a = set(first.split(","))
    b = set(second.split(","))
    print(a.intersection(b))
    print(sorted(a.intersection(b)))

    return ",".join(sorted(a.intersection(b)))




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
