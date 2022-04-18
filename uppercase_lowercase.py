# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor

def function(string):
    i=0
    count1=0
    count2=0
    while i<len(string):
        if string[i].isupper():
            count1+=1
        elif string[i].islower():
            count2+=1
        i=i+1
    print("number of upper case:",count1)
    print("number of lower:",count2)
function("The quick Brow Fox")








