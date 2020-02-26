counter = 105
name = "Nilesh Joglekar"

height = 5.5

print(counter, name, height)

if counter == 100:
    print("We have the score")
elif counter < 110:
    print("We are almost there")
else:
    print("No Score")

i = 10

while i < 21:
    print("The count is: ", i)
    i = i + 1

for letter in 'Python':
    print('Current Letter :', letter)
print()
fruits = ['Banana', 'Apple', 'Mango']

for fruit in fruits:  # traversal of List sequence
    print('Current fruit :', fruit)

num = [1, 2, 3, 4, 5, 6]

for x in num:
    print("Value in Array num: ", x)
print("--------------------")
num1 = [10, 'ABC', 3.5, 20, 18]
for y in num1:
    print("Value in Array num: ", y)

val = int(input("Enter Any Number: "))
numarray = [10, 33, 45, 32, 44, 55, 29]

flag = 0;

for p in numarray:
    if p == val:
        print("Number found in List")
        break
else:
    print("Number not in the list")