idade = int(input("Qual sua idade:"))
if idade > 18:
    print("Voce tem {} anos entao voce e maior".format(idade))
elif idade < 16:
    print("Voce tem {} anos entao voce e de menor".format(idade))
elif idade == 16 or 17 or 18:
    print("Voce tem {} anos entao voce e emancipado".format(idade))