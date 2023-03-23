str=input("Enter the string: ")
rev=reversed(str)
if (list(str))==(list(rev)):
    print("The string is a palindrome string.")
else:
    print("Ther string is not a palindrome string")