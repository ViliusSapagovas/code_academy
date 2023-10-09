my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

print(my_list)

print(f"Sum of the list: {sum(my_list)}")

number_of_items = len(my_list)

print(f"Number of items: {number_of_items}")

res = 1

for item in my_list:
    
    res = res * item 

print(f"Multification: of the list {res}")

print(f"Maximum of the list {max(my_list)}")

    