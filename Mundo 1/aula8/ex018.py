import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print("""O ângulo de {} tem o SENO de {:.2f}
O ângulo de {} tem o COSSENO de {:.2f}
O ângulo de {} tem a TANGENTE de {:.2f}""".format(an, sen, an, cos, an, tan))
