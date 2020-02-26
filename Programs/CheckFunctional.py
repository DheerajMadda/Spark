a = 10
b = 20
c = 30


def numoperations(n1, n2, n3, codeBlock):
    result = codeBlock(n1, n2, n3)
    return result


print(numoperations(a, b, c, lambda p,q, r: max(p,q,r)))
print(numoperations(a,b,c, lambda p,q, r: sum([p, q, r])))
print(numoperations(a,b,c, lambda p,q, r: p *q*r))
