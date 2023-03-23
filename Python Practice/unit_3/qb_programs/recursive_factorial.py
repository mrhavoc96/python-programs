def factorial(n):
    if (n==1):
        return n
    else:
        return n*factorial(n-1)

print("enter the number")
n=int(input())

if n<0:
    print("no factorial find can do for numbers.. negative.")
elif n==0:
    print("factorial is 1")
else: 
    print("factorial is: ",factorial(n))
