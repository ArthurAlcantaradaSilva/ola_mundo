#Desafio 008/Aula7
#Escreva um programa que leia um valor em metros e o exiba convertido em centimatros e milímetros.
print('Esse programa vai ler um valor em metros e vai converter e centimatros e milímetros.')
a = float(input('Digite o valor: '))
km = a/1000
hm = a/100
dam = a/ 10
dm = a*10
w = a*100
e = a*1000
print('O valor digitado {}m e os valor foi calculado e os valores em decímetro {}dm,'.format(a,dm),end = ' ')
print('em centimatros {}cm e milímetros {}mm.'.format(w,e))
print('{}Km,{}Hm e {}Dam '.format(km,hm,dam))