def max_function(numbers):
    i=0
    max=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    print(max)
max_function([3, 5, 7, 34, 2, 89, 2, 5])

        