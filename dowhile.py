"""
do while
Codigo para adivinhar um numero
"""
palpite = 0

numero = 9
#!= Indica diferenca
while palpite != numero:
    print("Adivinhe qual o numero correto?")
    palpite = int(input(":"))


print("Parabens voce acertou")
#print("Voce errou")





print(bool(palpite))