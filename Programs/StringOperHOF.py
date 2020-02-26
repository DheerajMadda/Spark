
str = "Hello World"

str1 = ["Now", "I", "Wonder", "What", "It", "Is"]


def stroperations(s, codeBlock):
    result = codeBlock(s)
    return result


print(stroperations(str, lambda x: x.lower()))
print(stroperations(str, lambda x: x.upper()))
print(stroperations(str, lambda x: x[::-1]))

print(list(map(lambda x: "".join(reversed(x)), str1)))
