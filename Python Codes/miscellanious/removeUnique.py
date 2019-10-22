# Your optional code here
# You can import some modules or create additional functions


def checkio(data: list) -> list:
    kz= [i for i in data if data.count(i) > 1]
    print(kz)
    uni_list=[]
    for i in data:
        if data.count(i) == 1:
            uni_list.append(i)
    return [i for i in data if i not in uni_list]




if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
