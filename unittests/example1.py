#https://www.youtube.com/watch?v=6tNS--WetLI
def add(x,y):
    return x+y


def sub(x,y):
    return x-y

def divide(x,y):
    if y == 0:
        raise ValueError('zero divisino')
    return x/y
print(add(4,5))




