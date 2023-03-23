def bigof3(a,b,c):
    if a>b and a>c:
        print("a is the biggest")
    elif b>c and b>a:
        print("b is the biggest")
    else:
        print("c is the biggest")
    
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

bigof3(a,b,c)