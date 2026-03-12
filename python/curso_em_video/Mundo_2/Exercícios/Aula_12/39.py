# Desafui 039 / Aula 12
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora da se alistar
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

def limpar():
    from os import system, name
    system("cls" if name == "nt" else "clear")

def linhas():
    print("="*75)

ano = date.today().year

linhas()
print(f"Esse e o ano atual {ano}")
linhas()
print("M = Mulher \nH = Homem.")
linhas()
sex = input("Digite seu sexo: ").lower()
linhas()
ano_n = int(input("Digite o ano de nascimento: "))
linhas()

idade = ano - ano_n
if sex == "h" or sex == "homem":
    limpar()
    linhas()
    if ano_n <= 0:
        print("Digite um ano valido.")
    elif idade == 18:
        print(f"Você já pode se alistar no serviço militar porque você tem {idade} anos \ne nasceu em {ano_n}.")
    elif idade >= 19:
        print(f"Já pasou de hora de você se alistar porque você tem {idade} anos e você já \npoderia se alistar com 18 anos em {idade - 18} ano atrais.")
    elif idade <= 17:
        print(f"Você não pode se alistar no serviço militar porque você tem {idade} anos e nasceu \nem {ano_n}, é o ano atual {ano} logo falta {18 - idade} ano para você se alistar.")
    else:
        print("Digite algo valido.")
elif sex == "m" or sex == "mulher":
    limpar()
    linhas()
    print("Você é uma mulher, e não tem obrigatoridade de se alistar no exercito.")
    print("Mas idade mínima e de 18 anos de idade, e logo abaixo vai \nmostrar se você podera se alistar.")
    linhas()
    if ano_n <= 0:
        print("Digite um ano valido.")
    elif idade >= 18:
        print(f"Você já pode se alistar no serviço militar porque você tem {idade} anos \ne nasceu em {ano_n}.")
    elif idade <= 17:
        print(f"Você não pode se alistar no serviço militar porque você tem {18 - idade} anos \ne nasceu em {ano_n}.")
    else:
        print("Digite algo valido.")
else:
    print("Digite H ou M para dar certo ou escreva de forma correta.")
linhas()