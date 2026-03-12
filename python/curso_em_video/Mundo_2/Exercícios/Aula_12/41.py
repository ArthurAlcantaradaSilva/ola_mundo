# Desafio 041/ Aula 12
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: Mirim
# - Até 14 anos: Infantil
# - Até 19 anos: junior
# - Até 20 anos: Sênior
# - Acima: Master
from datetime import date

def linhas():
    print("="*50)

linhas()
ida = int(input("Digite o ano de nascimento: "))
linhas()

ano = 0
ano = date.today().year

d = ano - ida

print(f"A sua idade é {d}")
linhas()

if d <= 13:
    print("Você é MIRIM.")
elif d <= 14:
    print("Você é INFANTIL.")
elif d <= 19:
    print("Você é JUNIOR.")
elif d <= 20:
    print("Você é SÊNIOR.")
else:
    print("Você é MASTER.")
linhas()
