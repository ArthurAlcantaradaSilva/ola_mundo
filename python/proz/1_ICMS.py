print("-"*40)
print("Esse programa vai calcular o valor do \nquilowatt a ser pago conforme a tabela.")
print("-"*40)
print("O valor do quilowatt é de: R$0,12 \nE acrescido do ICMS que é de: 18%")
print("-"*40)

i = int(input("Digite o valor comsumido de quilowatt: "))
if i > 0:
  p = i * 0.12
  print(f"O valor ser pago R$: {(p * 0.18) + p :.2f}")
else:
  print("Digite o valor de quilowatt, maior que 0.")