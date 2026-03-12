#Desafio 004/Aula 06
#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ele.
print('Esse programa vai tentar mostrar os tipos primitivo')
print('Só um aviso o programa vai ler com verdadeiro ou falso e eles estaram em True=Verdadeiro e o Falso=False.')
i = input('Digite alguma coisa:')
u = (i.isnumeric())
uu = (i.isalpha())
y = (i.isalnum())
yy = (i.islower())
t = (i.isupper())
tt = (i.istitle())
print('O tipo dele e só númerico:{}'.format(u))
print('O tipo dele e só letras:{}'.format(uu))
print('O tipo dele e,pode conter uma deles letras e números:{}'.format(y))
print('O tipo está em minúsculo:{}'.format(yy))
print('O tipo está em maiúsculo:{}'.format(t))
print('Está capitalizada:{}'.format(tt))# Correção
print(('O tipo de primitivo'),type(i))# Correção