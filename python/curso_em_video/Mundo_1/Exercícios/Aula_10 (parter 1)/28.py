# Aula 10 / Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# eschido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

def linhas():
    print("-=-"*20)

linhas()
num = int(input("Digite o seu popite: "))
linhas()

print("Eu estou pensando...")
linhas()

ran = randint(0,5)

sleep(1)

if num == ran:
    print(f"Você a certou o aleatorio era {ran} e o seu foi {num}")
    linhas()

else:
    print(f"Você errou o número era {ran} o seu foi {num}")
    linhas()
