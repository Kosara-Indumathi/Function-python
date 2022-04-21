def function(list):
    i=0
    max=0
    while i<len(list):
        if list[i]>max:
            max=list[i]
        i=i+1
    return max
print(function([2,4,1,8,6]))


