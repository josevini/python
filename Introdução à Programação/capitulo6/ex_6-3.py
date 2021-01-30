# Exercício 6.3 - Livro

l1 = []
l2 = []
l3 = []
while True:
    num = int(input('Informe um valor para a primeira lista (0 para parar): '))
    if num == 0:
        l3.extend(l1)
        break
    if num not in l1:
        l1.append(num)
while True:
    num = int(input('Informe um valor para a segunda lista (0 para parar): '))
    if num == 0:
        l3.extend(l2)
        break
    if num not in l2:
        l2.append(num)
print('Terceira lista: ', l3)
