VOWELS = list("aeiouy")
CONSONENTS = list("bcdfghjklmnpqrstvwxz")

def translate(phrase):
    phrase = list(phrase)
    i = 0
    char = []
    while i < len(phrase):
        if phrase[i] in VOWELS:
            char.append(phrase[i])
            i = i+2
        elif phrase[i] in CONSONENTS:
            char.append(phrase[i])
            i = i+1
        elif phrase[i].isspace():
            char.append(phrase[i])

        i = i + 1
    print(''.join(char))
    return ''.join(char)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
