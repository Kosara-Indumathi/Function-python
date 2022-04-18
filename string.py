# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
# "4",  "5" --> "9"
# "34", "5" --> "39"

# a="4","5"
# b=list(a)
# i=0
# while i<len(b):
#     c=int(b[i])+int(b[i+1])
#     i=i+2
# print(c)

def generate_range(min, max, step):
    out = []
    for i in range(min, max+1, step):
        out.append(i)
    return out
print(generate_range(2,10,2))