from functools import reduce

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]



x =10


def listOper(mlst, k, codeBlock):
    result = codeBlock(mlst, k)
    return result


print(listOper(lst, x, lambda m, t: m.count(t)))

print(listOper(lst, x, lambda m, t: t in m))

print(reduce(lambda y, z: y*z, lst))

print("The minimum no. in the list:", min(lst))
