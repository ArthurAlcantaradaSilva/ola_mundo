#Aula 09 / Desafio 024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# Santa luzia

def linhas():
    print("="*50)

linhas()
cidade_1 = input("Digite o nome da sua cidade: ").upper().strip().split()
linhas()

#cidade_1 = cidade.strip().split()
sei = ("SANTA" in cidade_1 [0] or "SANTO" in cidade_1 [0])

print(f"{sei}")