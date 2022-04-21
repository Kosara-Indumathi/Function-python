def function(list):
    i=0
    b=0
    a=[]
    while i<len(list)-1:
        b=list[i]-list[i+1]
        c=str(b)
        a.append(c)
        i=i+2
    print(a)
function([1,2,3,4,5,6])

 