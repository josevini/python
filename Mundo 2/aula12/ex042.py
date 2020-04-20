r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif (r1 == r2) and (r1 != r3) or (r1 == r3) and (r1 != r2) or (r3 == r2) and (r3 != r1):
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
