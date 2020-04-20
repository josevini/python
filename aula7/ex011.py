L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
area = L * A
tinta = area / 2
print("""Sua parede tem a dimensão de {}x{} e sua área é de {}m².
Para pintar essa parede, você precisará de {}l de tinta.""".format(L, A, area, tinta))
