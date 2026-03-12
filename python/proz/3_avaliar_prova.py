print("-"*50)
print("Esse programa vai ler uma nota e vai avaliar a nota do aluno.")
print("A nota parar ser aprovado e 60.0 ater 80.0.")
print("A nota parar ser reprovado e 59.5 pra baixo. ")
print("Notas invalidas são 0 e 80,5 pra cima.")
print("-"*50)
o = float(input("Digite a nota do aluno: "))
if o > 80.5 or o <= 0:
    print("NOTA INVÁLIDA.")
if o >= 60.0 or o == 80.0:
    print("O aluno foi aprovado")
elif  o == 59.5 or o >= 1.0:
    print("O aluno foi reprovado")
