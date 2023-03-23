def leapcheck(year):
    if (year%4==0) and (year%100!=0):
        print("The year is leap year")
    elif(year%400==0):
        print("The year is leap year")
    elif (year%100==0):
        print("The year is not a leap year")
    else:
        print("The year is not a leap year")

print("Enter year:")
year=int(input())
leapcheck(year)