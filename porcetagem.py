numero = float(input("Qual o preco do produto que vai sofrer desconto:"))
desconto = float(input("Quanto vai ser o desconto em procentagem:"))
p1 = numero*desconto
p2 = p1 / 100
descontototal = numero - p2
print("O produto que custa R${:.2f} vai passar a custar R${:.2f}".format(numero,descontototal))