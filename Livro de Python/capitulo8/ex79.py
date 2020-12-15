# Exercício 8.10 - Livro

def fibonacci(n):
    fibo = 1
    while n > 1:
        fibo *= n
        n-=1
    return fibo

for x in range(7):
    print(f'fibonacci({x}) = {fibonacci(x)}')



