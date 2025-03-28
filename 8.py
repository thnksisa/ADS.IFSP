'''Faça um programa que leia o ano de nascimento de uma pessoa e imprima se ela é
maior ou menor de idade. Declare o ano atual e o limite de maioridade como
constantes simbólicas.'''

# Definindo constantes simbólicas:

ANO_ATUAL = 2025
LIMITE_MAIOR = 18

# INÍCIO

print("Insira seu ano de nascimento:")
ano = int(input("➔ "))

idade = ANO_ATUAL - ano

if idade < 0:
    print("Não existe idade negativa.") 
elif idade >= LIMITE_MAIOR:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
