def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter number: "))

print("The fibonacci sequence is: ")
for i in range(n):
    print(fibonacci(i))