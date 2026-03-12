#Aula 09 / Desafio 026
#Faça um programa que leia uma frase pelo teclado e mostre:
#> Quantas vezes que aparece a letra "A".
#> Em que posição ela aparece a primeira vez
#> Em que posição ela aparece a última vez.

def linhas():
    print("="*100)

linhas()
fra = input("Digite uma frase: ").lower().strip()
linhas()
print(type(fra))
print (f"""Sua frase tem esse quantidade de A: {fra.count("a")} ela a pareceu na {fra.find('a') +1} e a utima vez foi { fra.rfind('a') +1} e o tamanho 
da frase {len(fra) - fra.count(" ")}.""")
linhas()