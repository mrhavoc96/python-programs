def multiply(x,y):
    return lambda x,y: x*y

x=int(input("Enter x: "))
y=int(input("Enter y: "))

z=multiply(x,y)
print(z(x,y))
