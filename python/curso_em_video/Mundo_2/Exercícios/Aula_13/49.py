# Desafio 049 / Aulas 13
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando um laço for.

def li():
    print("="*50)

li()
esc = float(input("Digite o seu número: "))
li()
for c in range(1,10):
    print(f"{c} x {esc} = {c*esc}")
li()