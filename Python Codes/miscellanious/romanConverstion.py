def reverse_roman(roman_string):
    rom = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':100}
    num = 0
    for i in roman_string:
        if i in rom:
            num = num+rom[i]
    print(num)
    return num
    #replace this for solution


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');