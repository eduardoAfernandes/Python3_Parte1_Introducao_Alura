import forca
import adivinhacaovFinal

print("***********************************")
print("********Escolha o seu jogo!********")
print("***********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
    print("Jogando forca!!")
    forca.jogar_forca()
elif(jogo == 2):
    print("Jogando adivinhação!!")
    adivinhacaovFinal.jogar_adivinhacao()
