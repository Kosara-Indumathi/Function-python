# Define a function which takes one parameter(positive integer). This function returns the sum of all multiples of 3 and 5 (not neccessary common multiples) in the range 1 to the integer passed as the parameter.
def function(a):
    i=0
    sum=0
    while i<=a:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
a=int(input("enter the number"))
function(a)