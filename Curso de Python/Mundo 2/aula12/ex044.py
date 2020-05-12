print('LOJAS GUANABARA')
preço = int(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = (preço * 10) / 100
    novo_preço = preço - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novo_preço))
elif opção == 2:
    desconto = (preço * 5) / 100
    novo_preço = preço - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, novo_preço))
elif opção == 3:
    novo_preço = (preço / 2)
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(novo_preço))
    print('Sua compra de vai custar R${:.2f}.'.format(preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        juros = (preço * 20) / 100
        novo_preço = preço + juros
        divisão = (novo_preço / parcelas)
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, divisão))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, novo_preço))
