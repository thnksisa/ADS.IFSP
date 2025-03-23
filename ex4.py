n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = n1, n2, n3

numeros_crescentes = sorted (numeros)

print(f"Os números em ordem crescentes são {numeros_crescentes}")