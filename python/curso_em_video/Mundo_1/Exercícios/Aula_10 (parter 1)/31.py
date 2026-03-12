# Aula 10 / Desafio 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

def linhas():
    print("="*50)

linhas()
km = int(input("Digite a quantidade de distancia da viagem Km: "))
linhas()

if km < 0:
    print("Você não vai viagar?? \nPorque sua distancia é 0 ou menor do que 0, então digite algo valido.")
    linhas()
elif km <= 200:
    print(f"A sua viagem vai custar R${km * 0.50 :.2f}")
    linhas()
    
else:
    print(f"A sua viagem vai custar R${km * 0.45 :.2f}")
    linhas()