arr = ['(hello)', ')yellow(', '((', ')', 'le())ft']
k1 = [j for i in arr for j in i]
def is_balanced(k1):
    count = 0
    for i in k1:
        if i == '(':
            count = count+1
        elif i == ')':
            count = count -1
    print(count)
    #if count < 0:
    #    print(count)
    #    return 'false'
    #if count == 0:
    #    print(count)
    #    return 'True'
    return count == 0
print(is_balanced(k1))

