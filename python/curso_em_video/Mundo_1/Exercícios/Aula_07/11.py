#Desafio 011/ Aula7
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m^2
print('Esse programa que vai calcular a sua área e a quantidade de latas de tinta')
m = float(input('Digite a altura: '))
n = float(input('Digite a abaser: '))
i = m*n
e = i/2
print('Esse foi altura {}, abaser {} e sua área {}m² e a quantidade litros é nescessárias e de {:.2}L'.format(m,n,i,e))