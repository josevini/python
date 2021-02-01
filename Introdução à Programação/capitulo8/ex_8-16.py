# Exercício 8.16 - Livro

def isPrimo(valor=0):
    if valor < 2:
        return False
    else:
        divisor = 1
        cont_divisor = 0
        while divisor <= valor:
            if valor % divisor == 0:
                cont_divisor += 1
            divisor += 1
        if cont_divisor > 2:
            return False
        else:
            return True

def numeroPrimo(total=0):
    valor = 1
    while True:
        if total < 1:
            break
        if isPrimo(valor):
            yield valor
            total -= 1
        valor += 1
numP = numeroPrimo(20)
print([num for num in numP])
