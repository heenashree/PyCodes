'''istrcmp('python', 'Python')
True
istrcmp('LaTeX', 'Latex')
True
istrcmp('a', 'b')
False
'''

#Method1
def istcomp(x,y):
    count = 0
    x = [i for i in x.lower()]

    y = [i for i in y.lower()]
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] == y[i]:
                count = count+1
            else:
                count = count-1
        if count == len(x):
            return ('True')
        else:
            return('False')
    else:
        return ('False')
print(istcomp('a', 'b'))

#Method2



