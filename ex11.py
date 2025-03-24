'''11. Elabore um programa que dado o peso de um boxeador, informe à categoria a qual
pertence, seguindo a tabela abaixo.'''

peso_str = input("Informe seu peso em kg: ")
peso=int(peso_str)

if peso <50:
    print("Você é da categoria palha!")
elif peso >=50 and peso <59:
    print("Você é da categoria pluma!")
elif peso >=59 and peso <75:
    print("Você é da categoria leve!")
elif peso >=75 and peso <87:
    print("Você é da categoria pesado!")
else:
    print("Você é da categoria super pesado!")

