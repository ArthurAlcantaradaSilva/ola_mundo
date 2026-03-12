# Desafio 036/ Aula 12
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e me quantos anos ele vai pagar.
# Calcule o valor da prestação mensal.sabendo que ela não pode exceder 30% do salário ou então o empréstimo sará negado.
def li():
    print("\033[32m=\033[m"*70)

li()
sa = float(input("Digite o seu salário R$: "))
cas = float(input("Digite o valor da casa R$: "))
ano = int(input("Digite quantos anos você vai pagar: "))
li()

mes = ano * 12
pacel = cas / mes
tax = sa * 0.3

if pacel < tax:
    print(f"O seu empréstimo foi aprovado e o valor que você vai ter que pagar é {pacel:.2f} por mês.")
else:
    print(f"O seu empréstimo foi reprovado pois, o seu salário é baixo ou o\nintem de compra e muito caro.")
li()