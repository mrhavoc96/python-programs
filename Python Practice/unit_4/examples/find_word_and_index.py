str='give up on your dreams and die'
word=input("Enter word to be found: ")
len=0
if word in str:
    print("The word",word,"is present in the string.")
    print("It's index is:",str.index(word))
    
else: 
    print("The word",word,"is not in the string :( ")