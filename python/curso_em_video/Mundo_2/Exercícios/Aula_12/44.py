#Desafio 44 / Aula 12
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

def linhas():
    print("\033[32m=\033[m"*50)

def limpar():
    from os import system, name
    system("cls" if name == "nt" else "clear")

linhas()
print("1 - pagar a vista em dinheiro com desconto de 10% \n2 - pagar a vista no cartão com desconto de 5%\n3 - pagar pacelado no cartão")
linhas()

esco = int(input("Digite a sua escolha: "))
linhas()

if esco == 1:
    limpar()
    linhas()
    print("Você escolheu pagar em dinheiro.")
    linhas()

    valor = float(input("Digite o valor a se pago R$: "))
    print(f"Esse e o preço final com desconto de 10% R$: {valor - (valor * 0.10)}")

elif esco == 2:
    limpar()
    linhas()
    print("Você escolheu pagar no cartão sem pacelar.")
    linhas()
    
    valor = float(input("Digite o valor a se pago R$: "))
    print(f"Esse e o preço final com desconto de 5% R$: {valor - (valor * 0.05)}")

elif esco == 3:
    limpar()
    linhas()
    print("Você escolheu pagar pacelado.")
    linhas()
    print("1 - para pacelar em 2x sem juros \n2 - para pacelar em 3x ou mais com juros de 20%")
    linhas()
    
    par = int(input("Digite a sua opição: "))
    linhas()
    
    if par == 1:
        limpar()
        linhas()
        print("Você escolheu pacelar em 2x sem juros.")
        linhas()

        valor = float(input("Digite o valor a se pago R$:"))
        print(f"Esse e o valor final pacelado em 2x sem juros R$: {valor / 2 :.2f}")
    
    elif par == 2:
        limpar()
        linhas()
        print("Você escolheu pacelar ater 3 ou mais \ncom juros de 20%.")
        linhas()

        valor = float(input("Digite o valor a se pago R$: "))
        parce = int(input("Digite a quantidade de pacelas: "))
        linhas()
        re = ((valor + (valor * 0.20)) / parce)
        print(f"Esse o valor finla pacelado em {parce}x com juros de 20% \nque você irar pagar em {parce} meses vai ", end = (""))
        print(f"ficar R${re :.2f} \ne no total R$: {valor + (valor * 0.20):.2f}")
        
    else:
        print("Você digitou um número invalido.")

else:
    print("Você digitou um número invalido.")
linhas()
