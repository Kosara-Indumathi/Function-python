# Write a Python program to reverse a string.
# Sample String : "1234abcd"
def function(string):
    i=1
    while i<=len(string):
        print(string[-i],end="")
        i=i+1
function("1234abcd")