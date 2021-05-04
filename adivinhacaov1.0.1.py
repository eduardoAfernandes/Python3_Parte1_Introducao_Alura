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

# Tudo que estiver indentado (4 espacos) pertence ao bloco da condicao
if(numero_secreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")


print("Fim do Jogo")
