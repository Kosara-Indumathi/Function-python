def perfect_number(a):
    i=1
    s=0
    while i<a:
        if a%i==0:
            s=s+i
        i=i+1
    if a==s:
        print(a,"perfect number")
    else:
        print(a,"not a perfect number")
a=int(input("enter the number"))
perfect_number(a)

