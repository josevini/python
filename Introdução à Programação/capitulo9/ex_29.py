# Exercício 9.29 - Livro

filmes = {
    'drama': ['Cidadão Kane', 'O Poderoso Chefão'],
    'comedia': ['Tempos Modernos', 'American Pie', 'Dr. Dolittle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Difícil de Matar'],
    'guerra': ['Rambo', 'Platoon', 'Tora! Tora! Tora!']
}

with open('txt/filmes.html', 'w', encoding='utf-8') as file:
    file.write("""<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Filmes</title>
    </head>
    <body>
    """)
    for c, v in filmes.items():
        file.write(f'<h1>{c}</h1>\n')
        for e in v:
            file.write(f'\t\t<p>{e}</p>\n')
    file.write(""" 
    </body>
</html>""")
