
num = str(input('Digite um valor na base 2: '))
if isBinary(num):
    res = conversor(num)
else:
    print('ERRO')
print(int(res))
