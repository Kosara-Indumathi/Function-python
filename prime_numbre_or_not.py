# Write a function to check if a number is prime or not.
def function(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("prime number")
    else:
        print("not a prime number")
a=int(input("enter the number"))
function(a)






