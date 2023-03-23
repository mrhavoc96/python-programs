str=input("Enter a word or sentence: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_count=0
for i in str:
    if i in vowels:
        vowel_count+=1

print("The vowels in ",str, "are ", vowel_count)
