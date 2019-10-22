def flat_list(array):
    flat=[]
    for i in array:
        print("member", i)
        if (str(i).strip('[')):
            k = (str(i)).strip('[')
            flat.append(k)
        elif(str(k)).strip(']'):
            k1=(str(i)).strip(']')
            flat.append(k1)
        else:
            flat.append(i)
    print(flat)




if __name__ == '__main__':
    #assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    #assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')