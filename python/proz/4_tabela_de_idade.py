print("-"*50)
print("Esse programa vai avaliar se você é um Aduto, criança, etc.")
print("-"*50)

p = int(input("Digite o seu ano de nacimento:"))
t = int(input("Digite o ano atual:"))

o = t-p

if o == 0 or o <= 3:
    print(f"A sua idade é {o} anos igaul de uma bebê .")
elif o == 4 or o <= 10:
    print(f"A sua idade é {o} anos igaul de uma criança.")
elif o == 11 or o <= 18:
    print(f"A sua idade é {o} anos igaul de um adolescente.")
elif o == 19 or o <= 50:
    print(f"A sua idade é {o} anos iagual de um adulto.")
elif o == 51 or o <= 100:
    print(f"A sua idade é {o} anos iagual de um idoso")
else:
    print("Invalidor porque não pode número negativo.")
    