# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
def function(list):
    i=0
    s=0
    while i<len(list):
        s=s+list[i]
        i=i+1
    print(s)
function([8,2,3,0,7])

