"""
Como descobrir se o numero eh impar ou par


"""
print("-"*30)
numero = int(input("Insira um numero para saber se eh impar ou par: "))

if (numero % 2) == 0:
    print(f"{numero} eh um numero par")
else:
    print(f"{numero} eh um numero impar")
print("-"*30)