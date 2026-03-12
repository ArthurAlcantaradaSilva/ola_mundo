# Aula 10 / Desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é (par) ou (ímpar)

def linhas():
    print("="*50)

linhas()
num = int(input("Digite um número: "))
linhas()

if num % 2 == 0:
    print(f"Esse número {num} e PAR.")
    linhas()
else:
    print(f"Esse número {num} e ÍMPAR.")
    linhas()
