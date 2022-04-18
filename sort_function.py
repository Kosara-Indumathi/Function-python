def sort_function(unorder_list):
    i=0
    length=0
    while i<len(unorder_list):
        if unorder_list[i]>=length:
            unorder_list.sort()
        i=i+1
    print(unorder_list)
sort_function([6, 8, 4, 3, 9, 56, 0, 34, 7, 15])


























