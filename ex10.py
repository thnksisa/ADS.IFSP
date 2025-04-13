'''
A convenção de graus Fahrenheit para Celsius é obtida pela fórmula C = 5. (F - 32)/9.
Escreva um programa que calcule e imprima uma tabela de graus centígrados em
função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes
simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5);
'''

f_input = float(input("Informe uma temperatura em Fahrenheit: "))
c_input = 5 * (f_input - 32) / 9
print(f"{f_input}°F equivale a {c_input:.2f}°C\n")

print("Tabela de conversão:")
print("Fahrenheit  |  Celsius")
print("------------------------")

for f in range(50, 151, 5):
    c = 5 * (f - 32) / 9
    print(f"{f:^11} | {c:^8.2f}")
