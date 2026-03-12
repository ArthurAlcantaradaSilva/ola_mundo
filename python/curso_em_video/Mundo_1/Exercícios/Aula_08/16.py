# Desafio 016/ Aula08
# Crie um programa que leia um número REAL qualquer pelo teclado e mstre na tela a sua porção INTEIRA.
# Ex.: Digite um númeor: 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc

print("="*51)
print("Esse programa vai ler um número real e vai mostra \nele inteiro sem arredondar para cima ou para baixo.")
print("="*51)
o = float(input("Digite o Número: "))
print("="*51)
print(f"O número real digitado foi {o} e sua pater inteiro é {trunc(o)}")
print("="*51)