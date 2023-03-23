str1=input("Enter first string: ")
str2=input("Enter second string: ")

if (str1.find(str2)==-1):
    print("The second string doesn't exist in the first string.")
else:
    print("The second string is present in first string.")