'''15. Construa um programa que receba três valores quaisquer e imprima-os em ordem
crescente. Como seu programa reage a valores de entrada iguais como no exercício
anterior? '''

a, b, c = input("Insira 3 valores separados com espaço: ").split( )
Lista_num = [a, b, c]

Lista_num.sort(key=int)
print(Lista_num)

#Ao inserir um ou mais valores identicos, eles sao repetidos durante a saida final
