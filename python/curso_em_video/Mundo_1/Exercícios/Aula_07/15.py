# Alua 7/ Desafio 15
# Faça um algoritmo que faça contagem de quantos dias de alugeuel de um carro.
print('Esse programa vai fazer o calculo do alugeuel que você tem que "pagar pelo carro"')
i = int(input('Digite quantos dias foi alugado: '))
u = float(input('Digite quantos Km rodados:  '))
y = 60*i+0.15*u
print('O quatidade de Km rodados foi {}Km e os dias alugado foi {} e valor para pagar foi R${:.2f}'.format(u, i, y))

#Aluguel Total
# = (Valor por dia × Número de dias) + (Valor por km rodado × Quilômetros rodados) + Taxas adicionais - Descontos
#o carro custa R$60 e por dia e R$0.15 por KM rodado