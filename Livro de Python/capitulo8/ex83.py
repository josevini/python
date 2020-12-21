# Exercício 8.15 - Livro

l = [1, 2, [3, 4, ['5']]]
spaces = 4
def showList(lis, level=0):
    for item in lis:
        if isinstance(item, list):
            print(' ' * (level * spaces), '[')
            showList(item, level + 1)
            print(' ' * (level * spaces),  ']')
        else:
            print(' ' * (level * spaces), item)
showList(l)
