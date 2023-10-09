
list_of_numbers = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	print(f"Write your {i+1} number : ")
	item = int(input())
	list_of_numbers.append(item)

print(list_of_numbers)

print(f"Your maximum number: {max(list_of_numbers)}")
