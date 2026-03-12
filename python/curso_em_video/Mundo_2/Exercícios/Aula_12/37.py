# Desafio 037 / Aula 12
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a vase de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal
def lin():
    print("="*50)

lin()
print("1 -> para Binário \n2 -> para Octal \n3 -> para Hexadecimal")
lin()
esc = int(input("Digite a sua escolha: "))
lin()

if esc == 1:
    n = int(input("Digite o seu número: "))
    print(f"Esse e o seu númeor convertido para Binário {bin(n)}.")
elif esc == 2:
    n = int(input("Digite o seu número: "))
    print(f"Esse e o seu número convertido para Octal {oct(n)}.")
elif esc == 3:
    n = int(input("Digite o seu número: "))
    print(f"Esse e o seu número convertido para Hexadecimal {hex(n)}.")
else:
    print("Digite um número de acordo com a tabela.")
 