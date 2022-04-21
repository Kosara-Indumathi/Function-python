def function():
    i=1
    a=[]
    while i<=30:
        a.append(i)
        i=i+1
    def fun():
        return a
    print(fun())
function()

