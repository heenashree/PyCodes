# find the missing number. do it by sum n*(n+1)/2 - (sum of all numbers)
a=[1,2,3,4,5,6,7,8,9,11,12]

k = len(a)
k1 = ((k)*(k+1))/2
sum_all = sum(a)
diff = k1 -sum_all
print(diff)
print(abs(int(diff)))

