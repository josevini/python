print('Gerador de PA')
print('-=' * 10)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
fim = 10
while c <= fim:
    print(p1, end=' → ')
    p1 += r
    c += 1
    if c > fim:
        print('PAUSA')
        termosAdicionais = int(input('Quantos termos você quer mostrar a mais? '))
        fim += termosAdicionais
print(f'Progressão finalizada com {fim} termos mostrados')
