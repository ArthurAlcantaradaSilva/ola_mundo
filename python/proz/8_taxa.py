print("="*50)
t = int(input("Digite o tempo em deposito:  "))
d = int(input("Digite seu dinheiro:  "))
print("="*50)

if t >= 5:
    m = (d-(0.95 * d))
    print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {m:.2f} ")
    print("="*50)

elif t == 4:
    p = (d-(0.9 * d)) 
    print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {p:.2f}")
    print("="*50)

elif t == 3:
     j = (d-(0.85 * d))
     print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {j:.2f}")
     print("="*50)

elif t == 2:
    k = (d-(0.75 * d))
    print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {k:.2f}")
    print("="*50)

elif t == 1:
    c = (d-(0.65 * d))
    print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {c:.2f}")
    print("="*50)

else:
    x = (d-(0.55 * d))
    print(f"o periodo de {t} e seu dinheiro {d} a taxa será: {x:.2f}")
    print("="*50)
 