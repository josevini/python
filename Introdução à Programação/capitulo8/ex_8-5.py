# Exercício 8.5 - Livro

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None
lista = ['Vinicius', 10, 'M']
print(pesquise(lista, 'M'))
