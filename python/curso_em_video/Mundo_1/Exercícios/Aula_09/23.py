#Aula 09 / Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena:8
#Milhar: 1

def linha():
    print("="*50)

linha()
num = input("Digite algun número: ")
linha()

#O meu
num.split()
#do professor
# num = str(nu)

print(f"Sua Unidade: {num [-1] } \nSua Dezena: {num [-2] } \nSua Centena: {num [-3] } \nSeu Milhar: {num [0] }")
linha()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
from math import trunc

num2 = int(input("Digite algun número: "))
linha()

print(f"Sua Unidade: {num2 % 10} \nSua Dezena: {trunc((num2 / 10) % 10)} \nSua Centena: {trunc((num2 / 100) % 10)} \nSeu Milhar: {trunc((num2 / 1000) % 10)}")