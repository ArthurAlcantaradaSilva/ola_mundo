def linha():
    print("\033[34m=\033[m"*50)

linha()
print("Esse programa vai mostrar o mês do ano de acordo \ncom o número.")
linha()
i = int(input("Digite o núemro do mês desejado: "))
linha()

if i == 1:
    print(f"É Janeiro, e o número digitado foi {i}.")
elif i == 2:
    print(f"É Fevereiro, e o número digitado foi {i}.")
elif i == 3:
    print(f"É Março, e o número digitado foi {i}.")
elif i == 4:
    print(f"É Abril, e o número digitado foi {i}.")
elif i == 5:
    print(f"É Maio, e o número digitado foi {i}.")
elif i == 6:
    print(f"É Junho, e o número digitado foi {i}.")
elif i == 7:
    print(f"É Julho, e o número digitado foi {i}.")
elif i == 8:
    print(f"É Agosto, e o número digitado foi {i}.")
elif i == 9:
    print(f"É Setembro, e o número digitado foi {i}.")
elif i == 10:
    print(f"É Outuvro, e o número digitado foi {i}.")
elif i == 11:
    print(f"É Novembro, e o número digitado foi {i}.")
elif i == 12:
    print(f"É Dezembro, e o número digitado foi {i}.")
else:
    print("Digite um número valido.")

linha()
