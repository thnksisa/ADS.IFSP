'''Uma indústria de alimentos congelados tem capacidade para estocar até 5 toneladas
de produto pronto para venda. Faça um programa que controle o estoque dessa
empresa, lendo do teclado a produção em kg de cada dia (sendo que uma produção
igual a zero é utilizada para encerrar a leitura
'''
EstoqueMaximo = 5000
Produtos = float(input("Insira a informações de KG: "))

while 0 >= Produtos:
    print(f"Produto igual a {Produtos} invalido")
    print("Insira um outro valor: ")
    break

else:
    if Produtos >= EstoqueMaximo:
        print("Estoque excedido")
    else:
        print(f"O valor em KGs é {Produtos}KG, disponivel no estoque")