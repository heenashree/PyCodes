def frequency_sort(items):
    if len(items) < 2:
        return items

    dict_={}
    listy=[]
    for i in items:
        dict_[i] = items.count(i)
    import operator
    sorted_x = sorted(dict_.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_x[0][0])
    from itertools import repeat
    l = []

    for i in sorted_x:
        print(i[0],i[1])
        l.extend(repeat(i[0], i[1]))

    print (l)
    return (l)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
