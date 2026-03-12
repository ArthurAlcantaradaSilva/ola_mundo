
def tempo():
    from time import sleep
    sleep(3)

def titulo():
    titos = "\033[0;33;40m>===_BANCO ALAN LIMA_===<\033[m"
    print(f"{titos:-^83}")

def linhas():
    print("="*70)

def limpar_tela():
    import os
    os.system("cls" if os.name == "nt" else "clear")

cor = {"limpa" : "\033[m",
        "verm" : "\033[0;31;40m",
        "verd" : "\033[0;32;40m",
        "nigrito" : "\033[7;37;40m",
        "azuc" : "\033[1;36;40m",
        "azu" : "\033[34;40m"
        }

linhas()
titulo()
linhas()
print("Bem vindo ao BANCO ALAN LIMA, a nossa equipe fica \nmuito feliz com você aquir")
linhas()
print("Bora criar uma conta???????")
linhas()
print(f"{cor['nigrito']}Quando você acabar de fazer sua conta você vai ter que fazer login. {cor['limpa']}")
linhas()

while True:

    nome_usú = input("Digite o seu e-mail: ").lower().strip()
    senha_usú = input("Digite o sua senha: ").strip()
    apelido = input("Digite o seu apelido ou jeito que você quer nós te chamamos: ")

    linhas()
    print(f"{cor['nigrito']}Analisando suas informções. {cor['limpa']}")
    linhas()
    tempo()
    if not (nome_usú.endswith("@gmail.com") or nome_usú.endswith("@hotmail.com")):
        limpar_tela()
        linhas()
        print(f"{cor['verm']}Seu e-mail está errado. {cor['limpa']}")
        linhas()
        continue
    if nome_usú.endswith("@gmail.com") or nome_usú.endswith("@hotmail.com"):
        print(f"{cor['verd']}Sua conta foi criada. {cor['limpa']}")
        break
    else:
        print(f"{cor['verm']}O seu e-mail está errado ou sua senha. {cor['limpa']}")
        
linhas()

limpar_tela()

linhas()
titulo()
linhas()
print(f"{cor ['nigrito']}Faça login. {cor ['limpa']}")
linhas()

while True:
    nome_2_usú = input("Digite o seu e-mail da sua conta: ").lower().strip()
    senha_2_usú = input("Digite a sua senha da sua conta: ").strip()
    linhas()
    print(f"{cor ['nigrito']}Analisando as informações. {cor ['limpa']}")
    linhas()
    tempo()
    
    if not (nome_2_usú.endswith("@gmail.com") or nome_2_usú.endswith("@hotmail.com")):
        linhas()
        print(f"{cor['verd']}O seu e-mail esta errado. {cor['limpa']}")
        linhas()
        continue
    if  nome_2_usú == nome_usú and senha_2_usú == senha_usú:
        break
    else:
        limpar_tela()
        linhas()
        print(f"{cor['verm']}Sua senha ou sue e-mail estar incorreto. {cor['limpa']}")
        linhas()
limpar_tela()

dinheiro_usú = 0
escolha = 0

while escolha != 4:
    limpar_tela()
    linhas()
    print(f"{cor['azuc']}Bem-vindo de volta{cor ['limpa']} {apelido} ")
    linhas()
    print(f"{cor ['azu']}Digite um dos números para escolher. {cor ['limpa']}")
    linhas()
    print("1- Olhar o seu saldo.")
    print("2- Retirar o seu dinheiro.")
    print("3- Depositar.")        
    print(f"4- {cor ['verm']}Sair {cor ['limpa']}")
    linhas()

    escolha = int(input("Digite a seu opção: "))
    linhas()

    if escolha == 1:
        limpar_tela()
    
        linhas()
        print(f"O seu saldo é R$:{cor ['verd']} {dinheiro_usú :.2f} {cor ['limpa']}")
        linhas()
        tempo()

    elif escolha == 2:
        limpar_tela()
        linhas()
        print(f"Esse é o seu dinheiro que você possui R$: {cor ['verd']} {dinheiro_usú :.2f} {cor ['limpa']}")
        linhas()
        retira_usú = float(input("Digite a quantidade que você desejatira: "))

        if retira_usú < 0:
            linhas()
            print(f"{cor ['verm']}Irmão digite algo na moral. {cor ['limpa']}")
            linhas()
            tempo()
        else:
            res = dinheiro_usú - retira_usú
            if res >= 0:
                linhas()
                dinheiro_usú -= retira_usú
                print(f"O seu dinheiro agora R$: {cor ['verd']} {res :.2f} {cor ['limpa']}")
                linhas()
            else:
                linhas()
                print(f"{cor['verm']}Não é possvel tira dinheiro do nada. {cor['limpa']}")
                linhas()
        tempo()

    elif escolha == 3:
        limpar_tela()
        linhas()
        print(f"O seu dinheiro R$: {cor ['verd']} {dinheiro_usú :.2f} {cor ['limpa']}")
        linhas()
        depositar = float(input("Digite a quantidade de dinheiro que vai ser depositado: "))
        linhas()
        print(f"Esse é o seu dinheiro agora R$: {cor ['verd']} { dinheiro_usú + depositar :.2f} {cor ['limpa']}")
        linhas()
        tempo()
        dinheiro_usú += depositar

    elif escolha == 4:
        limpar_tela()
        linhas()
        print(f"{cor ['nigrito']}Obrigado por esclher o banco ALAN LIMA, é volte sempre {cor ['limpa']} {apelido}")
        linhas()
        break

    else:
        limpar_tela()
        linhas()
        print(f"{cor['verm']}Digite algo valido. {cor['limpa']}")
        linhas()  
        tempo()                 
