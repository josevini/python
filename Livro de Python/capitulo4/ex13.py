# Exercício 4.2 - Livro

velocidade = float(input('Informe a velocidade do automóvel: '))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Você passou do limite de velocidade! Receberá uma multa de R${multa}')
print('Tenha um bom dia!')
