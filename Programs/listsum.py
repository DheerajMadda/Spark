my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0


def sumAll(lst):
    mytotal = 0
    for x in lst:
        mytotal = mytotal + x

    return mytotal


def sumOdd(lst):
    mytotal = 0
    for x in lst:
        if x % 2 != 0:
            mytotal = mytotal + x

    return mytotal


def sumEven(lst):
    mytotal = 0
    for x in lst:
        if x % 2 != 0:
            mytotal = mytotal + x

    return mytotal


def listoperation(lst, codeBlock):
        total1 = 0
        total1 = codeBlock(lst)
        return total1


print(listoperation(my_list, sumAll))
print(listoperation(my_list, sumOdd))
print(listoperation(my_list, sumEven))


i = 10
j = 20


def giveMeAdd():
    def add(a, b):
        return a + b
    return add


func = giveMeAdd()


print(func(i, j))



