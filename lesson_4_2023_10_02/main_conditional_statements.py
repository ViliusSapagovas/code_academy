# two options to describe variable

weight_lower_limit = 75.5
weight_higher_limit: float = 100.0

weight = float(input("Enter your weight: "))



# if weight > weight_higher_limit:
#     print("Mindaugas is kebab")
# print("Test is successful")

# if weight > weight_higher_limit:
#     if weight > 130:
#         print("WTF?")
#     print("Mindaugas is kebab")
# elif weight < weight_lower_limit:
#     print("Mindaugas is hungry")
# else :
#     print("Mindaugas is all good")

if weight > weight_higher_limit:
    print("Mindaugas is kebab")
elif weight < weight_lower_limit:
    print("Mindaugas is hungry")
else :
    print("Mindaugas is all good")

    