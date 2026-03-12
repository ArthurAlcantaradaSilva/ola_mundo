# Aula 10 / Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

def linhas():
    print("="*50)

linhas()
a = float(input("Digite um número: ")) 
b = float(input("Digite outro númro: "))
c = float(input("Digite o utimo número: "))
linhas()

lista = [a, b, c]
lista.sort()

print(f"Esse e o maior {lista [-1]} e esse é o menor {lista [0]}")
linhas()
