num = int(input('Digite um número para\n'
                'calcular o seu fatorial: '))
fat = 1
print(f'{num}! = ', end='')
while num != 1:
    fat *= num
    print(f'{num}', ' x ' if num > 2 else ' = ', end=' ')
    num -= 1

print(fat)
