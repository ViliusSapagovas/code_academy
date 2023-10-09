# Create a program, which takes 10 random numbers. The program should produce:
# 1. A list of non primary and tuple of primary numbers. 
# 2. After input is done, program should return the mathematical differnce //
# // between the highest and lowest number from non primary numbers, and sum of primary numbers from tuple.

# first_number = input("Enter your first number: ")
# second_number = input("Enter your second number: ")
# third_number = input("Enter your third number: ")

# list_of_numbers = [first_number, second_number, third_number]
# list_of_numbers_tupple = (first_number, second_number, third_number)

# print(list_of_numbers)
# print(list_of_numbers_tupple)


# Create a program, which takes 10 random numbers as user inputs.
# The program should produce list of input values what are less than 50 and tuple of all other values.
# After input is done, program should return the the mathematical differnce between the highest and lowest number //
#// from non primary numbers, and sum of primary numbers from tuple.

list_of_numbers = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	print(f"Write your {i+1} number : ")
	item = int(input())
	list_of_numbers.append(item)

New_list_of_lessthan50_numbers = []   

New_list_of_morethan50_numbers = []   

for i in range(0, n):
	if list_of_numbers[i] <= 50:
		New_list_of_lessthan50_numbers.append(list_of_numbers[i])
	else :
		New_list_of_morethan50_numbers.append(list_of_numbers[i])

print(New_list_of_lessthan50_numbers)
print(tuple(New_list_of_morethan50_numbers))

print(max(New_list_of_lessthan50_numbers) - min(New_list_of_lessthan50_numbers))

print(sum(New_list_of_morethan50_numbers))

New_list_of_prime_numbers = []
New_list_of_non_prime_numbers = []

# for i in range(0, n):
# 	x = list_of_numbers[i] 
# 	if x <= 3:
# 		New_list_of_prime_numbers.append(x)
# 	elif x >= 4:
# 		y = 2 
# 		while y < x:
# 			if x/y == 1:
# 				New_list_of_non_prime_numbers.append(x)
# 			else:
# 				y += 1
# 	else:
# 		New_list_of_prime_numbers.append(x)

for i in range(0, n):
	x = list_of_numbers[i] 
	y = 2 
	while y < x:
		if x % y == 0:
			New_list_of_non_prime_numbers.append(x)
			break
		else:
			y += 1
	else:
		New_list_of_prime_numbers.append(x)

print(tuple(New_list_of_prime_numbers))
print(New_list_of_non_prime_numbers)

print(f"Diffrence between highest and lowest non prime numbers: {max(New_list_of_non_prime_numbers) - min(New_list_of_non_prime_numbers)}")
print(f"Sum of prime numbers: {sum(New_list_of_prime_numbers)}")