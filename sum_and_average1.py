def function(num1,num2,num3):
    i=0
    s=0
    while i<num1:
        if num1>0:
            s=num1+num2+num3
            average=s/3
        i+=1
    print("sum",s)
    print("average",average)
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
function(num1,num2,num3)