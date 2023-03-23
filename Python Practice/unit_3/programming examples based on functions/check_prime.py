def prime_check(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                print("the number is not a prime number")
                break
        else:
            print("the number is a prime number")
    else:
        print("the number is a prime number")

n=int(input("Enter the number: "))
prime_check(n)
