from functools import reduce

from operator import add

i = 20
j = 30
k = 45

print(min(i, j, k))

lst = [2, 3, 4, 5]


squares = map(lambda x: x*x, lst)

print(list(squares))


name_lengths = map(len, ["Mary", "Isla", "Sam"])

print(list(name_lengths))


result = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

print(result)


sentences = ['Mary read a story to Sam and Isla.', 'Isla pushed Sam.', 'Sam Felt down']

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count('Sam')

print(sam_count)


people = [{'name': 'Mary', 'height': 160}, {'name': 'Isla', 'height': 80}, {'name': 'Sam'}]

heights = map(lambda x: x['height'], filter(lambda x: 'height' in x, people))


newlst = list(heights)
print(newlst)

if len(newlst) > 0:
    average_height = reduce(add, newlst) / len(newlst)
print(average_height)