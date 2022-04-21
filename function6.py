def function(list):
    i=1
    a=0
    even_sum=0
    odd_sum=0
    while i<=len(list):
        a=list[-i]
        print(a,end=",")
        if list[-i]%2==0:
            even_sum=even_sum+list[-i]
        else:
            odd_sum=odd_sum+list[-i]
        i=i+1
    print(even_sum)
    print(odd_sum)
function([1,2,4,6,8,3,5])