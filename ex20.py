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
moeda_ini = input("Digite a moeda de partida em maiúscula (D = dol, E = euro, L = libra, Y = yuan): ")
moeda_prox = input("Digite a moeda para conversão em maiúscula (D = dol, E = euro, L = libra, Y = yuan): ")
valor = float(input("Digite o valor a ser convertido na moeda de partida: "))
conversao = 0.0

# Conversão de moedas
dol_euro = 4.095/3.258
dol_lib = 4.529/3.258
dol_yuan = 0.515/3.258
euro_lib = 4.529/4.095
euro_yuan = 0.515/4.095
lib_yuan = 4.529/0.515

# Conversao entre moedas:
if moeda_ini == 'D':
     if moeda_prox == 'E':
        conversao = valor*dol_euro
     elif moeda_prox == 'L':
         conversao = valor*dol_lib
     else:
         conversao = valor*dol_yuan
elif moeda_ini == 'E':
     if moeda_prox == 'D':
         conversao = valor/dol_euro
     elif moeda_prox == 'L':
         conversao = valor*euro_lib
     else:
         conversao = valor*euro_yuan
elif moeda_ini == 'L':
     if moeda_prox == 'D':
         conversao = valor/dol_lib
     elif moeda_prox == 'E':
         conversao = valor/euro_lib
     else:
         conversao = valor*lib_yuan
else:
     if moeda_prox == 'D':
         conversao = valor/dol_yuan
     elif moeda_prox == 'E':
         conversao = valor/euro_yuan
     else:
         conversao = valor/lib_yuan

print("A conversão obtida é a de: ", conversao,".")
