# Desafio 020/ Aula8
# O mesmo professor do desafio anterior quer sortear a odem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem dos soteados.

from random import shuffle

print("="*50)
print("Esse programa vai ler quatro nomes vai sotear suas \nordens.")
print("="*50 )

o = input("Digite os nomes: ")
lista = o.split(",")
shuffle(lista)

print("="*50)
print(f"A ordem foi { ", ". join(lista)}.")
print("="*50)