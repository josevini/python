# Exercício 8.17 - Livro
def fibonacci(total=0):
    cont = 1
    p = 0
    n = 1
    while True:
        if total < 1:
            break
        if cont == 1:
            yield p
        elif cont == 2:
            yield n
        else:
            v = p + n
            p = n
            n = v
            yield v
        cont += 1
        total -= 1
print([num for num in fibonacci(8)])

