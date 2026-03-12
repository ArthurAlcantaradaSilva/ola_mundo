from os import system
from time import sleep
from math import cos,sin,tan,radians,sqrt

def linhas():
    print("="*50)

def limpar():
    system("cls") if "nt" else ("clear")

def tempo():
    sleep(3.5)

sei = "> Calculadora da impresa ALAN LIMA <"

escolha = 0

while escolha !=7:
    limpar()
    linhas()
    print(f"{sei:-^50}")

    linhas()
    print("1- Soma \n2- Subtração \n3- Divisão \n4- Multiplicação")
    print("5- Raiz quadrada \n6- Tangente, seno, cosseno \n7- Sair")
    linhas()

    escolha = int(input("Digite a sua escolha: "))
    linhas()

    if escolha == 1:
        limpar()
        linhas()
        print("A sua opção foi SOMAR.")
        linhas()

        n1 = float(input("Digite o primerio número: "))
        n2 = float(input("Digite o segundo número: "))

        linhas()
        print(f"A soma de {n1} e {n2} é igual a {n1 + n2}")
        linhas()
        tempo()

    elif escolha == 2:
        limpar()
        linhas()
        print("A sua opção foi Subtração.")
        linhas()

        n1 = float(input("Digite o primerio número: "))
        n2 = float(input("Digite o segundo número: "))

        linhas()
        print(f"A subtração de {n1} e {n2} é igual a {n1 - n2}")
        linhas()
        tempo()

    elif escolha == 3:
        limpar()
        linhas()
        print("A sua opção foi Divisão.")
        linhas()

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        linhas()
        print(f"A divisão de {n1} e {n2} é igual {n1 / n2}")
        linhas()
        tempo()

    elif escolha == 4:
        limpar()
        linhas()
        print("A sua opção foi mutiplicação.")
        linhas()

        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        linhas()
        print(f"A mutiplicação de {n1} e {n2} é igual de {n1 * n2}")
        linhas()
        tempo()

    elif escolha == 5:
        limpar()
        linhas()
        print("A sua opção foi raiz quadrada.")
        linhas()

        n1 = float(input("Digite o número: "))

        if n1 <0:
            linhas()
            print("Não é posivel pois o número e negativo.")
            linhas()

        else:    
            linhas()
            print(f"A raiz quadrada de {n1} é {sqrt(n1):.2f}")
            linhas()
        tempo()

    elif escolha == 6:
        limpar()
        linhas()
        print("A sua opção foi Seno, Cosseno e Tangente.")
        print("Só um detalhe você só precisa digitar um ângulo.")
        linhas()

        n1 = float(input("Digite o ângulo: "))
        radians(n1)

        linhas()
        print(f"O ângulo digitado foi {n1} sua Seno é {sin(n1) :.2f}, seu \nCosseno é {cos(n1) :.2f} e por fim a sua Tangente {tan(n1) :.2f}")
        linhas()
        tempo()

    elif escolha == 7:
        limpar()
        linhas()
        print("Obrigado, volte sempre.")
        linhas()

    else:
        limpar()
        linhas()
        print(f"Você digitou {escolha} que não é valido.")
        linhas()
        tempo()
