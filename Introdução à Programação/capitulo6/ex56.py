# Exercício 6.16 - Livro

numeros = [4, 1, 3, 5, 2]
fim = len(numeros)
while fim > 1:
    trocou = False
    pos = 0
    while pos < (fim - 1):
        if numeros[pos] < numeros[pos + 1]:
            trocou = True
            temp = numeros[pos]
            numeros[pos] = numeros[pos + 1]
            numeros[pos + 1] = temp
        pos += 1
    if not trocou:
        break
    fim -= 1
for numero in numeros:
    print(numero)
