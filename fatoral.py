"""
Programa que acha o fatorial de um numero
"""

numero = int(input("Insira o numero que voce quer descobrir o fatorial"))
fatorial = 1 
if numero < 0:
    print("Nao existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatorial de {numero} eh 1")
else:
    for x in range(1,numero+1):
        fatorial = fatorial*x
    print(f"O fatorial de {numero} eh: {fatorial} ")