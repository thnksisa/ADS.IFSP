'''Um microempresário tem por norma retirar mensalmente 40% do lucro de sua
empresa para os seus gastos pessoais se o lucro ultrapassar R$ 3.000,00 e retirar
apenas R$ 1.000,00 se o lucro for menor que isso. Faça um programa que leia do
teclado o faturamento mensal e o total das despesas para calcular o lucro (lucro =
faturamento - despesas) e imprima quanto o microempresário deve retirar neste mês.
Declare com constantes simbólicas o lucro mínimo, a retirada mínima e o limite da
retirada.'''

# INÍCIO

# Definindo constantes simbólicas:

LUCRO_MIN = 3000.00
RETIRADA_MIN = 1000.00
LIMITE_RETIRADA = 0.4

# Realizando o código:

faturamento = float(input("Qual o seu faturamento mensal?".replace(",",".")))
despesas = float(input("Qual o total de suas despesas?".replace(",",".")))

lucro = faturamento - despesas

if lucro > LUCRO_MIN:
    retirar = lucro * LIMITE_RETIRADA
    print("O microempresário deve retirar",(retirar),"neste mês.")
else:
    print("O microempresário deve retirar apenas 1.000,00 reais este mês.")