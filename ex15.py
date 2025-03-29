'''15. Construa um programa que receba três valores quaisquer e imprima-os em ordem
crescente. Como seu programa reage a valores de entrada iguais como no exercício
anterior? '''

a, b, c = input("Insira 3 valores separados com espaço: ").split( )
Lista_num = [a, b, c]
'''.split() faz com que quando os números sao inseridos como input,
eles sao separados com um espaço em vez de vígula.'''

Lista_num.sort(key=int)
print(Lista_num)
'''.sort arranja uma lista em ordem cresceste e o key=int faz com que todos os numeros na lista se tornem inteiros'''

#Ao inserir um ou mais valores identicos, eles sao repetidos durante a saida final
