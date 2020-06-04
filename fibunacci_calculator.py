# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

array = [5, 5, 6, 7, 8, 8]

def no_duplicates(array):
    new_array= []
    for item in array:
       if new_array.count(item) < 1:
           new_array.append(item)
    return new_array

print(no_duplicates(array))