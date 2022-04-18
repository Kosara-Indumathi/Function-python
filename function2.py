list=[4,3,2,8]
i=0
a=[]
while i<len(list):
    j=i
    while j<len(list)-1:
        b=str(list[i])+str(list[j+1])
        a.append(b)
        j=j+1
    i=i+1
print(a)









