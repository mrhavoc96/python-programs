str=input("Enter some letter or sentence: ")

digit_count=0
letter_count=0
for i in str:
    if(i.isdigit()):
        digit_count+=1
    else:
        letter_count+=1

print("the total number of letters in ",str, "are ", letter_count)
print("the total number of digits in ",str, "are ", digit_count)

