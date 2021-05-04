print("***********************************")
print("Bem vindo no jogo de adivinhacao!")
print("***********************************")

#variavel que guarda o numero que tem que ser adivinhado
numero_secreto = 42

#recebendo o que o usuario digitou e guardando na variavel chute (sempre vai ser string)
chute = input("Digite o seu número: ")
print("Voce digitou",chute)

#Convertendo a variavel chute que antes era do tipo string para um inteiro
chute = int(chute)

#Guardando a comparacao numero_secreto e chute (Boolean)
acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

# Tudo que estiver indentado (4 espacos) pertence ao bloco da condicao
if(acertou):
    print("Voce acertou!")
else:
    if(maior):
       print("Voce errou! O seu chute foi maior do que o número secreto!!")
    elif(menor):
        print("Voce errou! O seu chute foi menor do que o número secreto!!")

print("Fim do Jogo")
