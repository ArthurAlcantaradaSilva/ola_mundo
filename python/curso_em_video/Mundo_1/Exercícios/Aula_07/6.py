#Desafio 006/ Aula 7
#Crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada.
print('Esse programa vai calcular o dobro, o triplo e raiz quadrada do número digitado.:)')
a = int(input('Digite o número: '))
e = a*2
o = a*3
i = a**2 # Esse foi o meu jeito
# I = a ** (1/2) Esse foi do professor for correta
# pow(n (1/2))
print('O seu número digitado foi {}, e o seu dobro {},'.format(a,e), end=' ')
print('o seu triplo {} e sua raiz quadrada e {}'.format(o,i)) # estava errado porque está e levado oa quadrado