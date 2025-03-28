'''Em um determinado país, deve declarar imposto de renda todo cidadão com renda
anual superior à $ 23.750,00. A renda anual é a renda mensal multiplicada por 13 (12
meses mais a o 13o salário). A alíquota para quem paga é de 20%. Faça um programa
que leia do teclado a renda mensal do usuário e imprima se ele está isento ou se ele
deve fazer a declaração de renda e qual o imposto devido. Declare como constantes
simbólicas o limite para imposto: 23750; o fator de multiplicação: 13; e a alíquota:
20%.'''


renda_maxima = 23750
renda_mensal = float(input("Digite sua renda mensal R$: "))
renda_anual =  renda_mensal * 13
aliquota = 20


if renda_anual > renda_maxima:
   deconto_aliquota = (aliquota / 100) * renda_anual
   print(f"Sua renda anual foi {renda_anual:.2f},voce está apto para pagar imposto esse ano,seu desconto de aliquota desse ano é {deconto_aliquota:.2f}")
else:
   print(f"Sua renda anual foi {renda_anual:.2f},voce está inapto para pagar imposto esse ano")


''' Var atribuidas com valores no anuncia, com o calculo sendo feito com base na renda mensal e atribuido o desconto de aliquota, com a informação de renda anual''' 
