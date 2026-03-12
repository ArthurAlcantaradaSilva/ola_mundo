# Desafio 056 / Aula 13
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# 1. A média de idade do grupo.
# 2. Qual é o nome do homem mais velho.
# 3. Quantas mulheres têm menos de 20 anos.

def lp():
    from os import system, name
    system("cls" if name == "nt" else "clear")

def li():
    print("="*50)

li()
lista = []
num = 0
dd = []

for pes in range(2):
    no = input("Digite o seu nome: ")
    idad = int(input("Digite a sua idade: "))
    sexo = input("Digite se você é Homem ou Mulher: ").lower()
    lp()
    lista += no, idad, sexo
    num += idad

print(f"Esse é a media de idade do gurpo {num/2:.0f}")
print(f"Esse e a pessoa com a maior idade {dd}")