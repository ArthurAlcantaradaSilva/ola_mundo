print("="*50)
tempo = int(input("Digite o tempo de trabalho: "))
print("="*50)

if tempo >=0 and tempo <= 40:
  print(f"Você trebalho essa quatidade de tempo {tempo} que foi \nmenor do que 40", end = (" ")) 
  print(f"hora trabalhadas e seu \nsalário foi R${tempo*15}.")
  print("=" *50)

elif tempo >= 40:
  print(f"Você trabalhou essa quantidade de tempo {tempo} que \nfoi maior do que 40", end = (" "))
  print(f"horas trabalhadas e seu \nsalario foi R${((tempo % 10 ) *21) + 600 :.2f}.")
  print("=" *50)

else:
   print("Valor de horas trabalhadas está errada.")
