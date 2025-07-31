import random
print("#########################")
print("#  jogo de adivinhaçao  #")
print("#########################")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100
print("Qual niveis de dificuldade?  ")
print("(1) - facil (2) - medio (3) - dificil ")

nivel = int(input("Escolha um nivel"))

if(nivel == 1):
  print("seu patinho ")
  totaltentativas  = 20
elif (nivel == 2):
    print("fraco")
    totaltentaivas = 10
elif(nivel == 3):
    print("konan")
    totaltentativas = 5

