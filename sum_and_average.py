def average_sum(list):
    i=0
    s=0
    while i<len(list):
        if list[i]>0:
            s=list[i]+s
            average=s/len(list)
        i+=1
    print("sum=",s)
    print("average=",average)
average_sum([3,4,5])




