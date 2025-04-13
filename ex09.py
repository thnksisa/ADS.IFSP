''''
Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
acumulados. Faça um programa que compute o progresso do aluno, através da
3
leitura de suas notas até que ele termine o 10º nível. Utilize o comando break (por
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
máxima).
'''



nivel = 1

while nivel <= 10:
    print(f"\n--- Nível {nivel} ---")
    tentativas = 0
    pontos_acumulados = 0
    
    while tentativas < 5:
        nota = int(input(f"Tentativa {tentativas + 1} - Insira sua nota: "))
        tentativas += 1
        
        if nota == 100:
            print("Nota máxima! Avançando de nível.")
            nivel += 1
            break
        else:
            pontos_acumulados += nota
    else:  
        if pontos_acumulados < 300:
            nivel -= 1
            if nivel < 1:
                nivel = 1
            print(f"Você acumulou apenas {pontos_acumulados} pontos. Voltou para o nível {nivel}.")
        else:
            print(f"Você acumulou {pontos_acumulados} pontos. Permanece no nível {nivel}.")
