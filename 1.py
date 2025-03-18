'''Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
valor até R$100,00 ganha um cupom para concorrer a um carro e se ele comprar
acima de R$100,00 ganha dois cupons e um vale-desconto no total de 10% da
compra. Faça um programa que leia do teclado o total de compras e imprima se o
cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
desconto.'''

# Constantes simbólicas:

LMT_COMPRA = 100.00
PORCENTAGEM_DESC = 0.1

# Comando de entrada de dados:

valorC = float(input("Insira o valor da sua compra: ").replace(",", "."))

# Condição: 

if valorC <= LMT_COMPRA:
    print("Sua compra foi no valor de {:.2f} reais. Você tem direito a um cupom para concorrer a um carro.".format(valorC))
else:
    desc = valorC * PORCENTAGEM_DESC 
    descTotal = valorC - desc

    print("Sua compra foi no valor de {:.2f} reais. Você recebeu um vale-desconto 10OFF! "
    "Com o desconto aplicado, sua compra ficará no valor de {:.2f} reais. "
    "\n Além disso, você ganha dois cupons para concorrer a um carro.".format(valorC, descTotal))

# Fim.