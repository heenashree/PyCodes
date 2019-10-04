from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    '''
    #Solution 1
    if len(elements) < 2:
        return True
    else:
        k = elements[1]
        for i in elements[1:]:
            if i is not k:
                return False
        return True
        '''
    #Solution 2
    '''
    
    if len(elements) >= 2:
        element = [elements[0]] * len(elements)
        if element == elements:
            return True
        else:
            return False
    '''
    #Solution 3


    element = elements[1:] + elements[:1]
    print("elements", element)
    if element == elements:
        return True
    else:
        return False





if __name__ == '__main__':
    #print("Example:")
    #print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")