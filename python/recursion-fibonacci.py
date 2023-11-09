#generate n fibonacci number

#normal method
def fibo(n):
    a,b=0,1
    for i in range(1,n):
        a,b=b,a+b
    return a

n=int(input("Enter number\n"))
print(n,"th element without recursion",fibo(n))

    
#recursion

def fibonacci(n):
    if n==0:return 0
    if n==1:return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print('Using recursion',fibonacci(n-1))
