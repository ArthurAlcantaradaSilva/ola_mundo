#Aula 09 / Desafio 027
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#Último = Souza

def linhas():
    print("="*55)

linhas()
nome = input("Digite o seu nome completo: ").strip().split()
linhas()

print(f"O seu primeiro nome é {nome [0]} e no fim do seu nome é {nome [-1]}.")
