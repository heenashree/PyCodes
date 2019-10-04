def checkio(text: str) -> str:
    #solution ONe
    '''
    letters = [ch for ch in text.lower() if ch.isalpha()]
    letter_count = {ch: letters.count(ch) for ch in set(letters)}
    return max(sorted(letter_count), key=letter_count.get)
    '''

    list_text = [k.lower() for k in text]
    print(list_text)
    k = [list_text.count(i) for i in list_text]
    data = dict(zip(list_text,k))

    # Make dictionary with only alphabets
    new_data={}
    for key,value in data.items():
        if key.isalpha():
            new_data[key] = value

    elements = list(data.values())
    element = [elements[0]] * len(elements)
    sorted_list = sorted(list_text)
    sorted_again = [i for i in sorted_list if i.isalpha()]

    if elements == element:
        return sorted_again[0]
    else:

        k_data = [key for key, value in new_data.items() if value == max(new_data.values())]

        return (sorted(k_data)[0])

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Lorem ipsum dolor sit amet") == "m", "Hello test"
    assert checkio("fsbd") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")