'''12. Uma empresa decidiu dar um bônus de Natal aos seus funcionários, cujo valor é
definido do seguinte modo:
a. Funcionários do sexo masculino com tempo de casa superior à 15 anos terão
direito à um bônus de 15% do seu salário.
b. Funcionárias com tempo de casa superior à 10 anos terão direito a um bônus
de 25% do seu salário.
c. Demais funcionários receberão um bônus de R$ 500,00
Elabore um programa que leia os dados necessários e calcule o bônus à que tem
direito o empregado. '''

tempo_str = input("Insira seu tempo de colaboração em anos: ")
sexo_str = input("Indique seu sexo como M (masculino) ou F (feminino): ")
tempo = int(tempo_str)

if tempo >15 and sexo_str == "M" or sexo_str == "m":
 print("Você tem direito a 15% de bônus!")
elif tempo >10 and sexo_str == "F" or sexo_str == "f":
 print("Você tem direito a 25% de bônus!")
else:
 print("Você tem direito a R$500,00 de bônus!")
