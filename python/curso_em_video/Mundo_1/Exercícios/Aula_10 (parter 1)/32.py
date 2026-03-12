# Aula 10 / Desafio 032
# Faça um programa que leia um ano qualquer e mostre se ele é (BISSEXTO).

from datetime import date

def linhas():
    print("="*50)

linhas()
ano = int(input("Digite um ano: "))
linhas()

if ano == 0:
    ano = date.today().year # date == data / today == hoje / year == ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"Esse {ano} ano é Bissexto.")
    linhas()
else:
    print(f"Esse {ano} ano não é Bissexto.")
    linhas()
