# Exercício 3.9 - Livro
hora = int(input('Informe a hora: '))
minuto = int(input('Informe os minutos: '))
segundo = int(input('Informe os segundos: '))
segundos = segundo + (minuto * 60) + ((hora * 60) * 60)
print(f'{hora}h, {minuto}min, {segundo}seg equivalem a {segundos} segundos')
