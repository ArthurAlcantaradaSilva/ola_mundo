# Aula 7/ Dessafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('Esse algoritmo vai ler um salário e vai mostrar o seu aumento')
e = float(input('Digite o salário: '))
t = int(input('Digite o seu aumento: '))
y = e*(t/100)

#Eu não sabi Por que dividir por 100
#Quando você escreve 15%, isso significa "15 por 100", ou seja, 15/100 = 0.15. Em matemática,
#para calcular uma porcentagem de um valor

h = y+e
print("O seu salário {:.2f} e seu aumento {}% e por fim o seu reajuste {:.2f}.".format(e,t,h))

#Se um funcionário recebeu R$ 2.000,00 no mês anterior e o reajuste é de 7%, o novo salário será de R$ 2.140,00.
