#Aula 09 / Desafio 025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

def linhas():
    print("="*50)

linhas()
nome = input("Digite o seu nome: ").lower()
linhas()

nome.strip()
li = nome.split()

if "silva" in li:
    print("Você tem Silva no nome.")
    linhas()
else:
    print("Você não tem Silva no nome.")
    linhas()
#///////////////////////////////////////////////////////

print("silva" in nome)