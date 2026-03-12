# Desafio 043 / Aula 12
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# 6,4 media de erro
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: 
def linhas():
    print("="*50)

linhas()
al = float(input("Digite a sua altura: "))
pe = float(input("Digite o peso: "))
linhas()

media = pe/(al * al)

print(f"Esse e seu peso de acordo com o calculo do IMC")
print("\033[34m=\033[m"*50)
if media < 0 :
    print("O resutaldo deu 0, logo está errado.")
elif media <= 18.5:
    print(f"A baixo do peso {media:.1f}.")
elif media <= 25:
    print(f"Peso iadeal {media:.1f}.")
elif media <= 30:
    print(f"A cima do peso {media :.1f}.")
elif media <= 40:
    print(f"Obesidade {media :.1f}.")
elif media > 40:
    print(f"Obesidade Mórbida {media :.1f}.")
else:
    print("Deu erro.")
linhas()
