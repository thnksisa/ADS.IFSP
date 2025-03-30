'''
17. Escreva um programa que leia os três lados de um triângulo e imprima se o triângulo
é equilátero, isósceles ou escaleno, ou ainda, se estes lados não podem constituir um
triângulo.
Lembre-se que:
• O comprimento de cada lado de um triângulo é sempre menor do que a soma
dos comprimentos dos outros dois lados.
• Triângulo equilátero: três lados iguais.
• Triângulo isósceles: dois lados iguais.
• Triângulo escaleno: três lados diferentes.
'''

#Lados:
a = float(input("Digite o tamanho do lado 'a': "))
b = float(input("Digite o tamanho do lado 'b': "))
c = float(input("Digite o tamanho do lado 'c': "))

# Função Modular
def mod(x):
    if x < 0:
        # se x for negativo, inverte para positivo:
        return -x
    else:
        return x

# Desigualdade Triangular (verificação de existência de triângulo)
if a + b <= c:
    print("Valores inválidos para formar um triângulo.")
elif c <= mod(a - b):
    print("Valores inválidos para formar um triângulo.")

# Verificação do tipo de Triângulo:
else:
    if a == b == c:
        # se todos os lados forem iguais:
        print("Este é um triângulo equilátero.")
    elif a == b or a == c or b == c:
        # se algum lado for igual a outro:
        print("Este é um triângulo isósceles.")
    else:
        # se todos os lados forem diferentes:
        print("Este é um triângulo escaleno.")

