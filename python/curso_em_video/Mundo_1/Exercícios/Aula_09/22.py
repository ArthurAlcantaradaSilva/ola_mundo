#Aula 09 / Desafio 022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#> O nome com todas as letras maiúsculas.
#> O nome com todas minúsculas.
#> Quantas letras ao todo (Sem considerar espaços).
#> Quantas letras tem o primeiro nome.
def linha():
    print("="*70)

linha()
nome = input("Digite o seu nome completo: ").strip()
linha()

print(f"O seu nome com todas letras em maiúsculas: {nome.upper()}")
print(f"O seu nome em minúsculos: {nome.lower()}")
print(f"A quantidade de letras que o seu nome tem: {len(nome) - nome.count(" ")}")
pri_nome = nome.split(" ")
print(f"O seu primeiro nome que é ({pri_nome [0]}), tem esse quantidade de letras: {len(pri_nome [0])}")
linha()
