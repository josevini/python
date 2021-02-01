# Exercício 8.11 - Livro

def valida_string(string, minimo, maximo):
    string_length = len(string)
    if string_length < minimo or string_length > maximo:
        return False
    else:
        return True
res = valida_string('Eu', 1, 5)
print(res)
