# Desafio 046 / Aula 13
#Faça um programa que mostre na tela uma contagem regressiva para o estoura de forgos de aritificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep

def li():
    print("\033[34m=\033[m"*50)

li()
for c in range(10,0-1,-1):
    print(c)
    sleep(1)
li()
