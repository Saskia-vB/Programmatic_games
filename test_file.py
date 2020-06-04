array = [5,5,4, 6, 7, 8, 9, 10, 10]

def no_duplicates(array):
    new_array= []
    for item in array:
        if new_array.count(item)<1:
            new_array.append(item)
    return new_array

print(no_duplicates(array))