def fun(list):
    i=0
    sum=0
    count=0
    while i<len(list):
        if list[i]<0:
            sum=sum+list[i]
        elif list[i]>0:
            count=count+1
        i=i+1
    print(sum,",",count)
fun([-1,-3,-4,-2,1,2,3])
