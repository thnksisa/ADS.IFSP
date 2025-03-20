'''Em uma loja de eletroeletrônicos, um vendedor que consiga vender mais de R$
3.000,00 por mês recebe como comissão 5% do valor vendido. Abaixo disso, ele não
recebe nenhuma comissão. Faça um programa que leia do teclado o total de vendas
mensais de um vendedor e imprima se ele tem direito a comissão e, se tiver, de
quanto.'''

# Definindo variáveis:

salario = float(input("Insira o seu valor total de vendas mensais:").replace(",","."))
comissao = 0.05
salarioCc = salario * comissao
salarioMin = 3000.00

# Início:

if salario >= salarioMin:
    salarioCc
    print("Você receberá uma comissão de {:.2f} reais.".format(salarioCc))
else:
    print("Você não receberá comissão.")

# FIM.
