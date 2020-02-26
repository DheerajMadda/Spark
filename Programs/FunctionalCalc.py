# Program make a simple calculator that can add, subtract, multiply and divide using functions

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def myoperation(p, q,codeBlock):
    result = codeBlock(p,q)
    return result



if choice == '1':
    print(num1, "+", num2, "=", myoperation(num1, num2, lambda a, b:  a + b))

if choice == '2':
    print(num1, "-", num2, "=", myoperation(num1, num2, lambda a, b:  a - b))

if choice == '3':
    print(num1, "*", num2, "=", myoperation(num1, num2, lambda a, b:  a * b))

if choice == '4':
    print(num1, "/", num2, "=", myoperation(num1, num2, lambda a, b:  a + b))
