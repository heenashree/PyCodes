from collections import Counter

X = int(input())
sizes = Counter(map(int, raw_input().split()))
N = int(input())
earnings = 0
print("Counter", sizes)

for i in xrange(N):
    size, x = map(int, raw_input().split())
    print(sizes[size])
    if sizes[size] > 0:
        sizes[size] -= 1
        earnings += x

print
earnings  # Enter your code here. Read input from STDIN. Print output to STDOUT

