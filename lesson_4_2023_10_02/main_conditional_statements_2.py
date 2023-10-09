# a = 50
# b = int(input("Enter b: "))

# if a >= b:
#     print(b)
# else:
#     print(a)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a < b and b < c:
    print(f"first condition met: {b}")
elif a < c:
    print(f"Second condition met: {a}")
else:
    print(f"None of conditions was met: {a} {b} {c} {d}")

