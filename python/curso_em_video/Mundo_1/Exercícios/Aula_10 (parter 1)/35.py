# Aula 10 / Desafio 035
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podedm ou não
# formar um triângulo.

def linhas():
    print("="*50)

linhas()
a = float(input("Digite primeiro linha: "))
a2 = float(input("Digite segunda linha: "))
a3 = float(input("Digite terceira linha: "))
linhas()

if (a + a2) > a3 and (a + a3) > a2 and (a2 + a3) > a:
    print("É possivel fazer um triângulo.")
    linhas()

else:
    print("Não é possivel fazer um triângulo.")
    linhas()
    