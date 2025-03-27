'''Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
valor até R$100,00 ganha um cupom para concorrer a um carro e se ele comprar
acima de R$100,00 ganha dois cupons e um vale-desconto no total de 10% da
compra. Faça um programa que leia do teclado o total de compras e imprima se o
cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
desconto.'''



Compras = int(input("Digite quanto voce gastou:$ "))
Vale_desconto = 10

if Compras == 100:
    print("Voce ganhou um cupom para concorrer um carro")
else:
    Compras > 100
    desconto = ( Vale_desconto / 100) * Compras
    print(f"Voce ganhou dois cupons para concorrer a um carro, e um desconto no valor de {desconto:.2f}%")
