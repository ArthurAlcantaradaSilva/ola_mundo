# Aula 7/ desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Vai calcular o desconto de produtos e mostrar o seu novo preço')
j = float(input('Digite o valor do produto R$'))
e = float(input('Digite o desconto do produto:'))
i = (e/100)
o = i*j
u = j-o
print('O valor digitado foi R${} e o desconto {:.0f}% o seu novo preço com o desconto e {:.2f}'.format(j, e, u))