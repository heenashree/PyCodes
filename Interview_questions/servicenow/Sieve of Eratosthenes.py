#popular method to find the prime numbers smaller than given number
# n =10, prime = 2,3,5,7 4=2*2, 6=3*2, 8= 2*4, prime is numner 1 and number itself


#method 1
'''
n =10
for i in range(100):
    if i >1:
        for k in range(2,i):
            if i%k == 0:
                break
            else:
                print(i, "Prime")
                break

'''
#method 2
n = [n for n in range(0,200)]
p = [2,3,5,7]
k=[]
'''
Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p2, count up in increments of p and mark each of these numbers greater than or equal to p2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
'''
for w in p:
    for i in range(2,200):
        if w*(w+i) in n:
            n.remove(w*(w+i))
print("n", n)


