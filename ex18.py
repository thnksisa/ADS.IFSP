'''
18. Desejamos calcular, a partir do sexo e da altura, o peso ideal de uma pessoa. Para
isto, devemos saber que existem duas fórmulas para o peso ideal, que são:
• Homens: (72,7 * altura) - 58
• Mulheres: (62,1 * altura) - 44,7
Para que uma pessoa seja considerada obesa, a diferença entre o seu peso e o peso
ideal deve ser superior à 40 Kg. Elabore um programa que leia o sexo, o peso e a
altura de uma pessoa, imprima o peso ideal e informe se a pessoa está abaixo do
peso ideal, acima do peso ideal ou obesa.
'''

# Inserção de dados
sexo = input("Digite 'm' para masculino ou 'f' para feminino: ")
altura = float(input("Digite a altura (em m): "))
peso_atual = float(input("Digite o peso atual: "))
peso_ideal = 0.0

# Cálculo do peso ideal
if sexo == 'm':
    peso_ideal = 72.7*altura - 58
else:
    peso_ideal = 62.1*altura - 44,7

# Verificação em relação ao peso ideal
if peso_atual > peso_ideal + 40:
    print("A pessoa indicada está com obesidade.")
elif peso_atual < peso_ideal:
    # nesse caso, qualquer valor de peso abaixo do ideal é considerado abaixo do peso.
    print("A pessoa está abaixo do peso ideal.")
else:
    print("A pessoa está no peso ideal.")
