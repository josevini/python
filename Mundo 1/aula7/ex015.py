dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
print('-'*25)
Pdias = (dias * 60)
PKm = (km * 0.15)
print("""Preço por dias: R${:.2f}
Preço por Km: R${:.2f}
Total: R${:.2f}""".format(Pdias, PKm, Pdias+PKm))
print('-'*25)
