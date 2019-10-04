def time_converter(time):
    x, y = time.split(':')
    if int(x) < 12 and int(x) > 00:
        return (str(int(x)) + ":" + y + " a.m.")
    elif int(x) == 00 and int(y) == 00:
        return (str(12) + ":" + y + " a.m.")
    elif int(x) == 12 and int(y) < 59:
        return time + " p.m."
    elif int(x) > 12 and int(x) < 24:
        return (str(int(x) - 12) + ":" + str(y) + " p.m.")


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")