def isBinary(n):
    num = str(n)
    res = True
    for pos, bit in enumerate(num):
        if bit != '0' and bit != '1':
            res = False
    return res

def toDecimal(num):
    pot = len(num) - 1
    soma = 0
    for pos in range(0, len(num)):
        soma += (int(num[pos]) * (2 ** pot))
        pot -= 1
    res = soma
    return res

def getBinaryNumber(msg=''):
    while True:
        number = input(msg)
        if number.isnumeric():
            if isBinary(number):
                return number
            else:
                print('Número inválido!')
        else:
            print('Insira um número!')

def question(msg=''):
    while True:
        resp = str(input(msg)).lower()
        if resp == 's':
            return True
        elif resp == 'n':
            return False
        else:
            print('Tente novamente!')

def conversor():
    print('---' * 10)
    while True:
        num = getBinaryNumber('Digite um valor na base 2: ')
        resp = toDecimal(num)
        print(f'Decimal: {int(resp)}')
        resp = question('Quer sair? [S/N] ')
        print('---' * 10)
        if resp:
            break
        else:
            continue

def organiza(lista):
    cont = 0
    nova_lista = []
    for valor in lista:
        cont += 1
        if cont == 1:
            nova_lista.append(valor)
        else:
            if valor < min(nova_lista):
                nova_lista.insert(0, valor)
            elif valor > max(nova_lista):
                nova_lista.append(valor)
            else:
                for pos in range(0, len(nova_lista) + 1):
                    if valor not in nova_lista:
                        if valor < nova_lista[pos]:
                            nova_lista.insert(pos, valor)
    return nova_lista
