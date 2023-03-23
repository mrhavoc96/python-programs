def count_occur():
    data=dict()
    words=str.split()
    for word in words:
        if word in data:
            data[word]+=1
        else:
            data[word]=1
    return data

str=input("Enter a sentence: ")
print("The occurences are as follows: ",count_occur())