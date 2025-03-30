'''
19. Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte
forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for
da categoria “Gerente”, receberá 20% de aumento e os demais funcionários
receberão 15% de aumento. Faça um programa utilizando o comando if else aninhado
que leia do teclado o salário e a categoria do funcionário, calcule e imprima o seu
novo salário.
'''

# Inserção de Dados
cargo = input("Digite o cargo do funcionário ('t' para técnico,'g' para gerente e 'd' para os demais): ")
salario = float(input("Digite o valor de seu salário atual: "))

# Classificação do novo salário
if cargo == 't':
    salario = salario*1.3
    # atualiza o salário para 130% do valor original, ou seja, aumento de 30%
    print("O novo salário de técnico será: ",salario)
elif cargo == 'g':
    salario = salario*1.2
    # atualiza para 120%, aumento de 20%
    print("O novo salário de gerente será: ",salario)
else:
    salario = salario*1.15
    # atualiza para 115%, aumento de 15%
    print("O novo salário para os demais funcionários será: ",salario)

