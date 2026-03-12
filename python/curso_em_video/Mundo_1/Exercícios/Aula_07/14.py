# Alua 7/ Desafio 14
# Faça um algoritmo que faz a conversão de temperatura para C', f' e K
#Celsius para Fahrenheit: F = C x 1,8 + 32
#Fahrenheit para Celsius: C = 5/9 x (F - 32)
#Celsius para Kelvin: K = C + 273,15
print('Esse programa vai pegar o número digitado e vai mostrar as temperatura em C, F e K')
e = int(input('Digite um a temperatura em C: '))
c = e
f = e*1.8+32
k = e+273
print('O número digitado foi {} e a temperatura em Celsius {}C, Fahrenheit {}F e Kelvin {:.2f}K.'.format(e,c,f,k))