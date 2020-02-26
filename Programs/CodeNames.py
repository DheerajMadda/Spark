import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Bond']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(list(names))




