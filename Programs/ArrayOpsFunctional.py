numarray = [10, 30, 50, 200, 500, 45, 55, 97, 129, 123]
p = 10


def arrayOperations(myarr, codeBlock):
    result = 0
    for x in myarr:
        result = result + codeBlock(x)
    print(result)


# arrayOperations(numarray, lambda x: x)
# arrayOperations(numarray, lambda x: x if x < 500 else 0)

def sumEvenPosElements(myarr, codeBlock):
    # result = 0
    # i = 0
    # while i < len(myarr):
    #     if i % 2 != 0:
    #         result += myarr[i]
    #     i = i + 1
    # print(result)
     result = codeBlock(myarr)
     print(sum(result))

sumEvenPosElements(numarray, lambda x: x)


def addConstantToElements(myarr, num, codeBlock):
    #i = 0
    # while (i < len(myarr)):
    #     myarr[i] = codeBlock(myarr[i]) + num
    #     i = i + 1
    # print(myarr)
    result = codeBlock(myarr,num)
    print(list(result))

#addConstantToElements(numarray, p, lambda x:x)

newarray = map(lambda v:v+p,numarray)
print(list(newarray))

resultnew = sumEvenPosElements(numarray,lambda x: x[1::2])


print(resultnew)


addConstantToElements(numarray, p, lambda x,p:map(lambda x:x+p ,x))
