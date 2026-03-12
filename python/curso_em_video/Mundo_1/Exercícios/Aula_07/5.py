#Desafio 005/Aula 7
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessoe seu antecessor.
print('Esse programa vai ler um número inteiro e mostrar o seu sucessor e seu antecessor.')
n = int(input('Digite o número: '))
o = n+1
e = n-1
print('O número digitadd foi {} e seu sucessor e {}, e seu antecessor {}.'.format(n,o,e))
# Foi o jeito que eu escrevir
print('O número digitadd foi {} e seu sucessor e {}, e seu antecessor {}.'.format(n,(n+1),(n-1)))
# Esse foi o jeito do professor