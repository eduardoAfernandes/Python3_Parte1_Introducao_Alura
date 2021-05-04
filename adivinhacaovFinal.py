#Importando o modulo random para gerar um numero aleatorio
import random


def jogar_adivinhacao():

    print("***********************************")
    print("Bem vindo no jogo de adivinhacao!")
    print("***********************************")

    #variavel que guarda o numero que tem que ser adivinhado
    numero_secreto = random.randrange(1,101)

    #Total de tentativas
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nível: "))

    #Validando o nivel de dificuldade
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 18
    else:
        total_tentativas = 5


    for rodada in range(1, total_tentativas + 1):
    #Interpolacao de String usando o metodo format
        print("Tentativa {} de {}".format(rodada, total_tentativas))
    #recebendo o que o usuario digitou e guardando na variavel chute (sempre vai ser string)
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou",chute_str)

    #Convertendo a variavel chute que antes era do tipo string para um inteiro
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!!!")
            continue


    #Guardando a comparacao numero_secreto e chute (Boolean)
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    # Tudo que estiver indentado (4 espacos) pertence ao bloco da condicao
        if(acertou):
            print("Voce acertou e fez {} pontos!!".format(pontos))
            break
        else:
            if(maior):
               print("Voce errou! O seu chute foi maior do que o número secreto!!")
            elif(menor):
                print("Voce errou! O seu chute foi menor do que o número secreto!!")
            pontos_perdidos = abs(numero_secreto - chute )
            pontos = pontos - pontos_perdidos
    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()
