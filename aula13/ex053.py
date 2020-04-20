frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
inverso = ''
for c in range(len(frase) - 1, -1, -1):

    inverso += frase[c]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
