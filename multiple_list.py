def multiple_list (list_change,list_change1):
    i=0
    a=[]
    while i<len(list_change):
        b=list_change[i]*list_change1[i]
        a.append(b)
        i=i+1
    print(a)
multiple_list([5, 10, 50, 20],[2, 20, 3, 5] )
    

