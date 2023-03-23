def power(n):
    return lambda a: a**n
x=power(2)
print(x(3))