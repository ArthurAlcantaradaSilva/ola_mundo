# Aula 10 / Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mesnagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

def linhas():
    print("="*50)

linhas()
carro = float(input("Digite a sua velocidade: "))
linhas()

if carro <= 80:
    print(f"Você estar no limente.")
    linhas()
else:
    print(f"Você o ultrapassou o limente de 80Km/h você \nvai ter que pagar uma multa de {(carro - 80) * 7 :.2f}")
    linhas()
