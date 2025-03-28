'''Escreva um programa que, dadas duas datas, determine qual delas ocorreu
cronologicamente primeiro. Para cada uma das duas datas, leia três números
referentes ao dia, mês e ano, respectivamente.'''


data1 = input("Digite uma data (dd/mm/aaaa): ")
data2 = input("Digite outra data (dd/mm/aaaa): ")

dia1, mes1, ano1 = map(int, data1.split("/"))
dia2, mes2, ano2 = map(int, data2.split("/"))

if (ano1 > ano2) or (ano1 == ano2 and mes1 > mes2) or (ano1 == ano2 and mes1 == mes2 and dia1 > dia2):
    print("A primeira data é mais nova.")
else:
    print("A segunda data é mais nova.")


'''comando reconhece datas, com a seperação em split, sendo atribuida em ordem de dia/mes/ano, após isto entra em if else para comparar qual é mais nova'''
