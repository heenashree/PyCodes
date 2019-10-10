FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
dict_of_num= {1:'one', 2:'two',3:'three',4:'four',5:'five', 6:'six', 7:'seven ', 8:'eight', 9:'nine', 10:'ten',
                  11:'eleven',12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
                  30:'thirty',
                  40:'forty',
                  50:'fifty',
                  60:'sixty',
                  70:'seventy',
                  80:'eighty',
                  90:'ninety',
                  100:'hundred'}


def checkio(number):
    if number in dict_of_num:
        return dict_of_num[number]
    else:
        print((number//100)%10)


    #replace this for solution
    return 'string representation of n'

if __name__ == '__main__':
    checkio(133)
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio(4) == 'four', "1st example"
    #assert checkio(133) == 'one hundred thirty three', "2nd example"
    #assert checkio(12) == 'twelve', "3rd example"
    #assert checkio(101) == 'one hundred one', "4th example"
    #assert checkio(212) == 'two hundred twelve', "5th example"
    #assert checkio(40) == 'forty', "6th example"
    #assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')