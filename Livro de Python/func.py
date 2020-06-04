def isBinary(n):
    num = str(n)
    res = True
    for pos, bit in enumerate(num):
        if bit != '0' and bit != '1':
            res = False
    return res

def conversor(num):
    pot = len(num) - 1
    soma = 0
    for pos in range(0, len(num)):
        soma += (int(num[pos]) * (2 ** pot))
        pot -= 1
    res = soma
    return res
