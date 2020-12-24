# Exercício 6.18 - Livro

dic = {}
palavra = str(input('Digite uma palavra: '))
for letra in palavra:
    total = palavra.count(letra)
    if letra not in dic and letra != ' ':
        dic[letra] = total
print(dic)
