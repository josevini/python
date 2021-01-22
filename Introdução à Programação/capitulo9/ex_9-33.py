# Exercício 9.33 - Livro

import sys
import os.path
import urllib.request

if len(sys.argv) != 2:
    print('ERRO')
    sys.exit(1)
dir = sys.argv[1]

pagina = open('imagens.html', 'w', encoding='utf-8')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Imagens PNG e JPG</title>
</head>
<body>
""")
pagina.write(f'Imagens encontradas no diretório: {dir}')
for entrada in os.listdir(dir):
    nome, extensao = os.path.splitext(entrada)
    if extensao in ['.jpg', '.png', '.jpeg']:
        caminho_completo = os.path.join(dir, entrada)
        link = urllib.request.pathname2url(caminho_completo)
        pagina.write(f"<p><a href='{link}'>{entrada}</a></p>")

pagina.write("""
</body>
</html>
""")
pagina.close()
