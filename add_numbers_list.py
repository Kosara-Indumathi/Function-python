# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the sum of the integers with the same position.
# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.
# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this
def add_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        a=list1[i]+list2[i]
        print(a)
        i=i+1 
add_numbers_list([50,60,70],[10,20,13] )
    