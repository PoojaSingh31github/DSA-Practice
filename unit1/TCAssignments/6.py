def fibonacci(n):
    seq=[]
    a, b=0,1
    for i in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq
n=10
print(fibonacci(10))    


def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*(factorial(num-1))
num=4
print(factorial(num))    