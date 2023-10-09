my_dictionary = {"name": "Vilius", "surname": "Sapagovas"}



# print(type(my_dictionary["phone"]))


# print(my_dictionary)

my_dictionary["car"] = "Tesla"

my_dictionary["age"] = 50

my_dictionary["phone_numbers"] = [15154863121, 4561594863, 15648743481]

another_dictionary = {"street": "Something st.", "house_number": 123, "zip_code": "LT-11111"}

my_dictionary["address"] = another_dictionary

# 2 methods printing values of keys

print(another_dictionary["zip_code"])

print(my_dictionary["address"]["zip_code"])

my_dictionary["car"] = "Volvo"

my_dictionary["address"]["house_number"] = 120

print(my_dictionary["address"]["house_number"])

print(my_dictionary.keys())

for value in my_dictionary.values():
    print(value)

# using FOR loop for printing
d = {'a': 10, 'b': 20, 'c': 30}
for key, value in d.items():
    print(key, value)


# updating
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
d1.update(d2)
print(d1)

# making dictionaries from lists

test_keys = ["Albert", "Tom", "Stephen"]
test_values = [1, 4, 5]
my_second_dictionary= dict(zip(test_keys, test_values))
print(my_second_dictionary)