# Desafio 019/ Aula8
# Um professor quer sortear um dos seus quatro alunos para aoagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles -> Alunos e escrevendo o nome do escolhido.

from random import choice

print("="*50)
print("Esse programa vai ler quatro nomes e vai sortear um deles.")
print("="*50)

i = input("Digite os nomes: ")
lista = i.split(",") 
print(lista)
print("="*50)
print(f"A o sorteado foi {choice (lista)}.")
print("="*50)