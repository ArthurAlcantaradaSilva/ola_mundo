# Desafio 040 / Aula 12
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado
def linhas():
    print("="*50)

linhas()
n1 = float(input("Digite o a sua nota: "))
n2 = float(input("Digite sua outra nota: "))
linhas()

n = (n1+n2) /2

print(f"As notas foi {n1:.1f} e {n2 :.1f}, a média do aluno é {n:.1f}")
linhas()

if n <= 5:
    print("Foi reprovado.")
elif n <= 6.9:
    print("Estar de recuperação.")
else:
    print("Foi aprovado")
linhas()
