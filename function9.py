list=[5,7,1,3,4,11,12,33,18,17,12,3]
i=0
b=0
a=[]
while i<len(list):
    j=1
    while j<len(list):
        b=str(list[i])+str(list[j+1])
        a.append(b)
        j=j+1
    i=i+1
print(a)
