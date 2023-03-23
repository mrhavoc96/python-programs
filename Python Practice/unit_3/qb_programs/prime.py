def primecheck(num):
    if num>1:
        for i in range (2,num):
            if num%i==0:
                print("the number is not prime")
                break
        else:
            print("the number is prime")
    else:
        print("the number is prime")

print("Enter the number: ")
num=int(input())
primecheck(num)