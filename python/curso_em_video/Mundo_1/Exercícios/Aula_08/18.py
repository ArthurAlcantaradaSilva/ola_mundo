# Desafio 018/ Aula8
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan,radians

print("="*70)
print("Esse programa vai mostrar o seno, cosseno e a tangente de um ângulo")
print("="*70)
 
o = float(input("Digite o ângulo: "))

#E o eu meu deu errado.

#Esse é do professor guarabara.
print("="*85)
print(f"O valor do SENO { sin(radians (o)) :.2f}, O valor do Cosseno { cos (radians (o)) :.2f}, O Tangente { tan (radians (o)):.2f}.")
print("="*85)
