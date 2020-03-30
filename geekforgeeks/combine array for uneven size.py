# a_1, b_1, a2, b2, a3, b3

a = [1,3,5,7]
b= [2,4,6,8,10]
c=[]
if len(a)<len(b):

    for i in range(len(a)):
        c.extend([a[i], b[i]])
    print(c)
c.extend(b[4:])
print(c)
