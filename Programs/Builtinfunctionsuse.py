numarray = [10, 30, 50, 200, 500, 45, 55, 97, 129, 123]


def arrayOperations(myarr, codeBlock):
    result = 0
    for x in myarr:
        result = result + codeBlock(x)
    print(result)

#arrayOperations(numarray, lambda x: x)

mystr = "Hello World"

newstr = mystr.replace("l",'')
print(newstr)
newstr = mystr.split(" ")
print(newstr[0])