print("="*50)
salario = int(input("digite o seu salario:  "))
f = int(input("Digite finamciamento: "))
print("="*50)

s = salario*5

if s >= f:
    print("financiamento concedido")
    print("="*50)
else:
    print("financiamento negado")
    print("=" *50)    