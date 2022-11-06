chave = input("Digite a base da sua senha: ")
senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "*"
    elif letra in "Bb": senha = senha + "!"
    elif letra in "Cc": senha = senha + "&"
    elif letra in "Dd": senha = senha + "("
    elif letra in "Ee": senha = senha + ")"
    elif letra in "Ff": senha = senha + "="
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra

print(senha)