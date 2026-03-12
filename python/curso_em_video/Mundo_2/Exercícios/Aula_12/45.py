#desafio 045 / Aula 12 
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

def linhas():
    print("\033[31m=\033[m"*55)

linhas()
usu = input("Digite \033[35mpedra, papel\033[m ou \033[35mtesoura\033[m: ").lower()
linhas()

oposto = ["pedra","papel","tesoura"]

sei = choice(oposto)

if usu == sei:
    print(f"Ele escolhue {sei} e você escolheu {usu} e que deu EMPATE.")

elif usu == "papel" and sei == "pedra":
    print(f"Ele escolheu {sei} e você escolheu {usu} e VOCÊ VENCEU.")

elif usu == "pedra" and sei == "tesoura":
    print(f"Ele escolheu {sei} e você escolheu {usu} e VOCÊ VENCEU.")

elif usu == "tesoura" and sei == "papel":
    print(f"Ele escolheu {sei} e cocê escolheu {usu} e VOCÊ VENCEU.")

elif usu != "":
    print("Você digitou algo que não é valido.")

else:
    print(f"Ele escolheu {sei} e você escolheu {usu} e VOCÊ PERDEU.")
linhas()
