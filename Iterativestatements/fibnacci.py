def fib(n):
    a=0;b=1;s=0
    for i in range(n):
        s+=a
        a,b=b,a+b
    return s
print(fib(6))
