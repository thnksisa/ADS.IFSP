'''
16. Uma equação do segundo grau é descrita genericamente por ax^2 + bx + c = 0.
Escrever um programa que leia os valores de a, b e c e resolva a equação do segundo
grau correspondente, imprimindo as raízes reais quando existirem ou avisando que
não existem raízes.
'''

# Inserção dos valores para a^2x + bx + c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
solucao1 = 0.0
solucao2 = 0.0

# Delta da raíz
delta = b**2 - 4*a*c

# Verificações de validade da equação e do delta
if a == 0.0:
    print("Equação inválida.")
elif delta < 0.0:
    print("Não há soluções reais para a equação inserida")

# Cálculo das raízes
else:
    solucao1 = (- b + (delta)**(1/2))/(2*a)
    solucao2 = (- b - (delta)**(1/2))/(2*a)
    print("O conjunto solução da equação inserida é: S {",solucao1,",",solucao2,"}.")

