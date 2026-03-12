# Aula 10 / Desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

def linhas():
    print("="*50)

linhas()
salario = float(input("Digite o seu salário: "))
linhas()

if salario < 0:
    print(f"Não entendi.")
elif salario <= 1250.00:
    print(f"O seu salário e menor do que R$1.250,00 por isso \nvocê vai ter um aumento de 15% no seu salário que \nvai ficar assim R${salario * 0.15 + salario:.2f}")
    linhas()
else:
    print(f"O seu salário e maior do que R$1.250,00 por isso \nvocê vai ter um aumento de 10% no seu saláro que \nvai ficar assim R${salario * 0.1 + salario:.2f}")
    linhas()
