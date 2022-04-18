def reverse_function(reverse_list):
    i=1
    a=[]
    while i<=len(reverse_list):
        b=reverse_list[-i]
        a.append(b)
        i=i+1
    print(a)
reverse_function(["Z", "A", "A", "B", "E", "M", "A", "R", "D"])