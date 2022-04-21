def fun(list):
    i=0
    a=[]
    b=""
    while i<len(list):
        b=b+list[i]
        i=i+1
    a.append(b)
    return a
print(fun(['12','34','25','46','0','67']))


