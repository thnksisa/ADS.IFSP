# Jogo da acentuação


# Cores no terminal:
verde = '\033[1;32m'
fim = '\033[0m'
negrito = '\033[1m'
vermelho = '\033[1;31m'
roxo = '\033[35m'
rosa = '\033[95m'
ciano = '\033[36m'

print(f"{ciano}-"*250)
print('''
       _                         _                              _                    /\/|       
      | |                       | |                            | |                  |/\/        
      | | ___   __ _  ___     __| | __ _    __ _  ___ ___ _ __ | |_ _   _  __ _  ___ __ _  ___  
  _   | |/ _ \ / _` |/ _ \   / _` |/ _` |  / _` |/ __/ _ \ '_ \| __| | | |/ _` |/ __/ _` |/ _ \ 
 | |__| | (_) | (_| | (_) | | (_| | (_| | | (_| | (_|  __/ | | | |_| |_| | (_| | (_| (_| | (_) |
  \____/ \___/ \__, |\___/   \__,_|\__,_|  \__,_|\___\___|_| |_|\__|\__,_|\__,_|\___\__,_|\___/ 
                __/ |                                                            )_)            
               |___/                                                                            
''')
print("-"*250)

print(f"{fim}{roxo}\n\nINÍCIO\n\n{fim}")

# Contabilizador de erros e acertos:
erro = 0
acerto = 0

while True:
    print(f"{negrito}1- A palavra {roxo}GENERICO{fim}{negrito} possui acento?{fim}{fim}")
    resposta = input("> ").lower()
    if resposta == "sim":
        print(f"{verde}Você acertou!{fim}")
        print("-"*50)
        print(f"{negrito}Como se escreve com acento?{fim}")
        acento_correto = input("> ").lower()
        if acento_correto == "genérico":
            print(f"{verde}Parabéns! Você acertou. {fim}")
            print("-"*50)
            acerto += 1
            break
        else:
            print(f"{fim}{negrito}{vermelho}Poxa, você errou! O correto é GENÉRICO.{fim}")
            print("-"*50)
            erro += 1
            break
    elif resposta == "nao" or resposta == "não":
        print(f"{negrito}{vermelho}Poxa, você errou!{fim}")
        print("-"*50)
        erro += 1
        break
    else:
        print(f"{rosa}Por favor, insira resposta de SIM ou NÃO.{fim}")
        continue


while True:
    print("1- A palavra IDEIA possui acento?")
    resposta = input("> ").lower()
    if resposta == "nao" or resposta == "não":
        print(f"{verde}Você acertou!{fim}")
        print("-"*50)
        break
    elif resposta == "sim":
        print("Poxa, você errou! O correto é IDEIA. Sem acento.")
        print("-"*50)
        erro += 1
        break
    else:
        print("Por favor, insira resposta de SIM ou NÃO.")
        print("-"*50)
        continue

print(f"Você acertou {acerto} palavras. 😁")
if erro == 0:
    print(f"Você errou zero palavras. Parabéns!! 😬")
else:
    print(f"você errou {erro} palavras. Que pena!! 😰")