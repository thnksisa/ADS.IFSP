'''O que acontece no programa anterior se a pessoa nasceu há 18 anos, mas ainda não
fez aniversário? Melhore o programa para que, neste caso, o programa pergunte se a
pessoa já fez aniversário ou não antes de imprimir o resultado.'''

# ENUNCIADO ANTERIOR:

'''Faça um programa que leia o ano de nascimento de uma pessoa e imprima se ela é
maior ou menor de idade. Declare o ano atual e o limite de maioridade como
constantes simbólicas.'''

# INÍCIO

# Definindo constantes simbólicas:

ANO_ATUAL = 2025
LIMITE_MAIOR = 18

# INÍCIO

print("Insira seu ano de nascimento:")
ano = int(input("Adicione aqui:"))

idade = ANO_ATUAL - ano

if idade > 18:
    print("Você é maior de idade.")
elif idade < 18:
    print("Você é menor de idade.")
else:
    print("Você já fez aniversário no ano de 2025?")
    aniversario = input("SIM/NÃO: ").lower()
    
    if aniversario == "sim" :
        print("Você tem 18 anos. É maior de idade")
    elif aniversario == "não" or "nao" or "NAO":
        print("Você ainda tem 17 anos. É menor de idade.")
    else:
        print("Resposta inválida.")
# FIM.