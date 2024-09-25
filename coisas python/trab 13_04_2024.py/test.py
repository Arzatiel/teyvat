numero = print(input("Digite um número:"))

if numero in range(100, 200):
    print ("{} está no intervalo!".format(numero))
else:
    print ("{} não consta no intervalo!".format(numero))