# Write a Python program to generate and print a list of first and last 5 elements where 
# the values are square of numbers between 1 and 30 (both included).
def function():
    i=0
    a=0
    b=[]
    while i<=30:
        a=i*i
        b.append(a)
        i=i+1
    print(b[1:6],b[26:])
function()













