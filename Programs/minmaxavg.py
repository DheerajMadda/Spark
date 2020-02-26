from functools import reduce
numarray = [40,5,30,80,100,400,430,500]

# result = max(numarray)
# print(result)
#
# result = min(numarray)
# result = sum(numarray)/len(numarray)

people = [{'name': 'Mary', 'height': 160}, {'name': 'Isla', 'height': 80}, {'name': 'Sam'}]

heights = map(lambda x: x['height'], filter(lambda x: 'height' in x, people))

def add(x,y):
    return x + y

newlst = list(heights)

if len(newlst) > 0:
    average_height = reduce(lambda x,y: x + y,newlst)/ len(newlst)
print(average_height)
