# Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
list=['aba', 'xyz', 'aba', '1221']
i=0
c=0
while i<len(list):
    a=list[i]              
                                               
    c=c+1
    i=i+1
print(c)