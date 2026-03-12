# Desafio 042 / Aula 12
# Refaça o DESAFIO 035 dos triâmgulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
def linhas():
    print("\033[31m=\033[m"*57)

linhas()
n1 = int(input("Digite um lado: "))
n2 = int(input("Digite o segundo lado: "))
n3 = int(input("Digite o teserio lado: "))
linhas()
if n1 < n3 + n2 and n2 < n1 + n3 and n3 < n2 + n3:
    print("É possivel fazer im triâmgulo.")
    linhas()
    if n1 != n2 and n1 != n3 and n2 != n3:
        print("E um triâmgulo do tipo Escaleno, é que todos os lados \nsão diferentes.")
    elif n1 == n2 and n2 == n3 and n3 == n1 :
        print("E um triâmgulo do tipo Equilátero pois, todos os lados \nsão iguais.")
    elif n1 != n2 != n3:
        print("E um triâmgulo do tipo Isósceles, e porque um dos dois \nlados são iguais.")
else:
    print("Não é possivel fazer um triâmgulo.")
linhas()