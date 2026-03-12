#Desafio 010/ Aula7
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#uss$1,00 = R$3,27
print('Esse programa vai fazer corversão de reais em dólares')
a = float(input('Digite o valor em reais R$:  '))
d = float(input('Digite o dólar hoje US$: '))
o = a/d
print('Os números digitados foi R${} e o dóla hoje US${} e o valor corversão US${:.2f}'.format(a,d,o))