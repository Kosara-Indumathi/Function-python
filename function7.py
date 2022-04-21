def function(user): 
    i=0
    a=0
    b=[]
    while i<len(user)-1:
       a=int(user[i])*int(user[i+1])
       b.append(a)
       i=i+1 
    print(b)
    j=0
    max=0
    while j<len(b):
        if max<b[j]:
           max=b[j]
        j=j+1
    print("the max number:",max)
user=str(input("enter the number"))
function(user)


