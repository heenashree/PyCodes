##https://www.geeksforgeeks.org/comprehensions-in-python/

print("Example 1")
array = [1,2,4,5,2, 6,10,9]

lit = [i for i in array if i%2 == 0]
print("**use lambda**")


print("*******************1********************")
print("Example 2")
lit2 = [i*i for i in array]
print(lit2)

print("*******************2********************")
print("Example 3")

dict1 = {x:x*x*x for x in array if x%2!=0}
print(dict1)

print("********************3*******************")
print("Example 4")
dict2={}
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
for k,v in zip(state,capital):
    dict2[k] = v
print(dict2)

print("using comprehension")
dict3 = {key:value for (key,value) in zip(state, capital)}
print("dict3", dict3)

print("*******************4********************")

print("Example 5")
setval = {key for key in array if key%2 == 0}
print(setval)