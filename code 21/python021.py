# working sequence 

def fib2(n):
    if n<=1:
        return n
    
    a,b=0,1
    for i in range(1,n+1):
        n=a+b
        a=b
        b=n
        
    return a

fib2(12)


    
