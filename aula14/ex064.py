soma = 0
qtdNum = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if not (num == 999):
        soma += num
        qtdNum += 1
print(f'Você digitou {qtdNum} números e a soma entre eles foi {soma}.')
