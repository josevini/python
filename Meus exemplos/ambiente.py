from func import isBinary, toBinary
num = str(input('Digite um valor na base 2: '))
if isBinary(num):
    res = toBinary(num)
    print(int(res))
else:
    print('ERRO')
