a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter one of the folowing operations '+' '-' '/' '*': ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
else:
    print("Calculator doesn't support this operation !")