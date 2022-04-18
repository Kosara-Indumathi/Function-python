# Write a Python program to print the even numbers from a given list.
def function(list):
    i=0
    a=[]
    while i<len(list):
        if list[i]%2==0:
            a.append(list[i])
        i=i+1
    print(a)
function([1, 2, 3, 4, 5, 6, 7, 8, 9])
        

