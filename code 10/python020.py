# a program that calculates the fabonicci number

def fib(n):
    if n==0 or n==1:
        return n
    else:
        a= fib(n-1)
        b= fib(n-2)
    return a+b
    
 v=fib(4)
