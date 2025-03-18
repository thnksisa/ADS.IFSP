'''Um programa didático para crianças consiste em pedir dois números inteiros
quaisquer para a criança e depois perguntar a soma desses dois números. Se a
resposta estiver certa, o programa imprime uma mensagem de incentivo. Se não, o
programa imprime o valor correto da soma. Implemente esse programa.'''

# adicionando valores à variáveis.
num1 = int(input("Insira um número inteiro: "))
num2 = int(input("Insira outro número inteiro: "))

print("A soma entre esses dois números é?")
resultadoaluno = int(input("➔  "))

if resultadoaluno == num1+num2:
    print("Parabéns, você acertou!")
else:
    print("Errado. O resultado correto é",(num1+num2),".")

# Fim.