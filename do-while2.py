"""
do while
Codigo para adivinhar um numero
"""
palpite = 5

numero = 9
#is significa eh
while bool(palpite) is True:
    print("Adivinhe qual o numero correto?")
    palpite = int(input(":"))
    if palpite == numero:
        print("Parabens voce acertou")
        #vai parar a repeticao
        break
    else:
        print("Voce errou")



#print("Parabens voce acertou")
#print("Voce errou")





print(bool(palpite))