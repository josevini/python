# Exercício 9.35 - Livro

import os.path, sys, urllib.request

mascaraEstilo = "'margin: 5px 0px 5px 0px;'"
def geraEstilo(nivel):
    return mascaraEstilo

def geraListagem(pagina, diretorio):
    nraiz = os.path.abspath(diretorio).count(os.sep)
    for raiz, diretorios, arquivos in os.walk(diretorio):
        nivel = raiz.count(os.sep) - nraiz
        pagina.write(f'<p style={geraEstilo(nivel)}>{raiz}</p>')
        estilo = geraEstilo(nivel + 1)
        for a in arquivos:
            caminhoCompleto = os.path.join(raiz, a)
            tamanho = os.path.getsize(caminhoCompleto)
            link = urllib.request.pathname2url(caminhoCompleto)
            pagina.write(f"<p style={estilo}><a href='{link}'>{a}</a>  ({tamanho} bytes)</p>")

if len(sys.argv) < 2:
    print('Digite o nome do diretório para coletar os arquivos!')
    sys.exit(1)

diretorio = sys.argv[1]

pagina = open('arquivos.html', 'w', encoding='utf-8')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
pagina.write(f'Arquivos encontrados a partir do diretório: {diretorio}')
geraListagem(pagina, diretorio)
pagina.write("""
</body>
</html>
""")
pagina.close()
