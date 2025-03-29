'''13. Elabore um programa que receba três valores quaisquer e imprima o menor valor dos
três lidos. O que acontece se o seu programa tiver lido dois ou mais números iguais
(Ex.: 1, 1, 3)?'''

a, b, c = input("Insira 3 valores separados com espaço: ").split( )
Lista_num = [a, b, c]
'''.split() faz com que quando os números sao inseridos como input,
eles sao separados com um espaço em vez de vígula.'''

menor = min(Lista_num)
print(menor)
''' min seleciona o menor numero em um lista'''

#ao inserir dois ou mais números iguais, o programa continua monstrando apenas um número como saída
