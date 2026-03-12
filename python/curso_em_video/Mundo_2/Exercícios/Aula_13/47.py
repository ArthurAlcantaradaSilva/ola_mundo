# Desafio 047 / Aula 13
# Crie um programa que mosrte na tela todos os números pares que estão
# no intervalo entre 1 e 50.

def li():
    print("\033[34m=\033[m"*50)

li()
for c in range (0,50+1,2):
    print(c)
li()