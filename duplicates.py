# remove dupliactes from list
# two lists
example_list = ['a', 'b', 'lemon', 'c', 'lemon', 'd', 'a','pineapple']
# no_duplicates = []

def remove_duplicates(example_list):
    no_duplicates = []
    for item in example_list:
        if no_duplicates.count(item) < 1:
            no_duplicates.append(item)
    return no_duplicates

print(remove_duplicates(example_list))

# iterate through first array
# append to other array


