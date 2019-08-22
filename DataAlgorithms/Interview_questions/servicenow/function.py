int f(int a) {
if(a<=0) return 0;
return f(a-1)+f(a-2) +1 - f(a-3)}

f(4) + f(3) + 1-f(2)

f(3)+f(2)+1-f(1)

f(2)+f(1)+1-f(0)

f()

