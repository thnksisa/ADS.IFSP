renda_maxima = 23750
renda_mensal = float(input("Digite sua renda mensal R$: "))
renda_anual =  renda_mensal * 13
aliquota = 20


if renda_anual > renda_maxima:
   deconto_aliquota = (aliquota / 100) * renda_anual
   print(f"Sua renda anual foi {renda_anual:.2f},voce está apto para pagar imposto esse ano,seu desconto de aliquota desse ano é {deconto_aliquota:.2f}")
else:
   print(f"Sua renda anual foi {renda_anual:.2f},voce está inapto para pagar imposto esse ano")