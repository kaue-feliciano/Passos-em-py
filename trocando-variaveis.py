#Trocando as variaveis




x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

#Usaremos uma variavel temporaria
temp = x
x = y
y = temp

#E por fim iremos mostrar a troca
print(f"O valor de x depois da troca: {x}")
print(f"O valor de y depois da troca: {y}")
