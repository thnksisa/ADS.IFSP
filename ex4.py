n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Faz o comparativo de valores e imprime na ordem crescente, com base nas condicionais.

if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2
if n1 > n2:
    n1, n2 = n2, n1

print(f"Os números em ordem crescente são: {n1}, {n2}, {n3}")


'''


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = n1, n2, n3

numeros_crescentes = sorted (numeros)

print(f"Os números em ordem crescentes são {numeros_crescentes}")



'''

