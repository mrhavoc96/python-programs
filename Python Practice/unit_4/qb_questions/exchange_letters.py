def exchange(string):
    changed=string[-1:]+string[1:-1]+string[:1]
    return changed

string=input("Enter the string to be changed: ")
print("The changed string is: ",exchange(string))

