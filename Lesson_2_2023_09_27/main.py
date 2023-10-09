# number_one = 26
# number_two = 25
# print(number_one + number_two)
# # print(number_one // number_two)

# name = "Code Academy"

# print(name.replace("Cod", "Mo")) 

# print(name)

# print(name[5:12])

# print(name[-7:-1])
# print(name[ :-12])


# zaidimas
# print("5"+"5") #python adds two string variables into one, doesn't calculate



# pirmoji uzduotis
 
user_name = input("Enter your name:")
user_age = input("Enter your age:")

user = f"{user_name} {user_age}"

print(user)

x= int(user_age)

user_year = 2023 - x

print("Year you were born: ", user_year)

# antroji uzduotis 

sentence = input("Enter your sentence:  ")

print("Your sentence backwards: ", sentence[::-1])

print("Every second letter: ", sentence[1::2])

# # Trecioji uzduotis

first = input("Write first number ")

second = input("Write second number ")

first_number = int(first)

second_number = int(second)

print("sum of two numbers: ", first_number + second_number)
print("subtration of two numbers: ", first_number - second_number)
print("division of two numbers: ", first_number / second_number)
print("multiplication of two numbers: ", first_number * second_number)
print("power of two numbers: ", pow(first_number,second_number))
print("power of two numbers: ", first_number ** second_number)

# Ketvirtoji uzduotis

sentence = input("Enter your sentence:  ")
replace_letters = str.maketrans({'a' : '4', 'b' : '8', 'e' : '3', 'f' : '7', 'g' : '9', 'h' : '4', 'i' : '1', 'l' : '1', 'o' : '0', 's' : '5' })
print("Your sentence in Leet (sort of): ", sentence.translate(replace_letters))
