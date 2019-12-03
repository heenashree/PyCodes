#a = ()
# a = 1,2
# a = (1,2,3)
#c = ((1,2,3),(2,3))
#print(a)

print (type(type))

print(1+True)


#by reference
a = [1,2,3]
print (id(a))
b = a
print (id(b))
b.append([4,5])
c = b
print (id(c))
c.append(6)
print(a,b,c)

a='DBS'
b = str('DBS')
c = ''.join(['D','B','S'])
print(a,b,c)

row = [
    [11],
    [12],
    [13]

]

#convert columns to row transends

#lambda question
#mutable (list, dict, set, int) [int is immutable]

#change of list inside a tuple
k = (1,[2,3], 4)
k[1][0] = -1
print(k)

#linked list
#sorted array, find the sum that equates to a number
# find rotation of a sorted list

