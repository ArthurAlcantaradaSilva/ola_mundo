# Desafio 017/ Aula8
# Faça um program que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hpotenusa.

from math import sqrt,hypot

print("="*57)
print("Esse programa vai ler o cateto oposto e cateto adjacente \ne vai mostrar sua hipotenusa.")
print("="*57)

o = float(input("Digite o cateto oposto: "))
i = float(input("Digite o cateto adjacente: "))
print("="*57)

# O meu
print(f"O cateto oposto digitado {o} e o cateto adjacente {i} \nagaro por fim a sua hipotenusa {sqrt((i**2) + (o**2)):.2f}.")
# O do Guarabara 
# print(f"O cateto oposto digitado {o} e o cateto adjacente {i} agara por fim a sua hipotenusa {hypot(o , i):.2f}.")
