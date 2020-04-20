from datetime import date
nasc = int(input('Ano de nascimento: '))
data = date.today().year
idade = (data - nasc)
print('Quem nasceu em {}, tem {} em {}.'.format(nasc, idade, data))
if idade < 18:
    saldo = (18 - idade)
    print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(data + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(data - saldo))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
