'''
20. Utilizando-se do comando if else aninhado, elabore um programa que:
• Mostre um menu de opções de conversão entre moedas (1 – dólar americano,
2 – euro, 3 – libra esterlina e 4 – yuan;
• Leia a escolha do usuário;
• Leia o custo em R$ (reais) da operação;
• Imprima o valor da transação na moeda escolhida, de acordo com os fatores
de conversão da tabela abaixo.
______Moeda______|___Valor_(R$)__|
 Dólar americano |     3,258     |
      Euro       |     4,095     |
 Libra esterlina |     4,529     |
      Yuan       |     0,515     |
'''

# Inserção de Dados
moeda_conv = input("Digite a moeda de partida em maiúscula (d = dol, e = euro, l = libra, y = yuan): ")
valor = float(input("Digite o valor em reais a ser convertido: "))
conversao = 0.0
moeda = ''

# Conversões
dolar = 3.258
euro = 4.095
libra = 4.529
yuan = 0.515

if moeda_conv == 'd':
    conversao = valor*dolar
    moeda = 'dólares'
elif moeda_conv == 'e':
    conversao = valor*euro
    moeda = 'euros'
elif moeda_conv == 'l':
    conversao = valor*libra
    moeda = 'libras esterlinas'
else:
    conversao = valor*yuan
    moeda = 'yuans'

print("O valor de ",valor," em ",moeda,"será de: ",conversao)
