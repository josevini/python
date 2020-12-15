# Exercício 8.12 - Livro

def valida_lista(s, l):
    if s in l:
        return True
    else:
        return False
res = valida_lista('ele', ['eu', 'tu', 'ele', 'nós', 'vós', 'eles'])
print(res)