# Exercício 6.2 - Livro

l1 = []
l2 = []
l3 = []
while True:
    num = int(input('Informe um valor para a primeira lista (0 para parar): '))
    if num == 0:
        l3.extend(l1)
        break
    l1.append(num)
while True:
    num = int(input('Informe um valor para a segunda lista (0 para parar): '))
    if num == 0:
        l3.extend(l2)
        break
    l2.append(num)
print('Terceira lista: ', l3)
