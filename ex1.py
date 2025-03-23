Compras = int(input("Digite quanto voce gastou:$ "))
Vale_desconto = 10

if Compras == 100:
    print("Voce ganhou um cupom para concorrer um carro")
else:
    Compras > 100
    desconto = ( Vale_desconto / 100) * Compras
    print(f"Voce ganhou dois cupons para concorrer a um carro, e um desconto no valor de {desconto:.2f}%")
