'''
Questão 5

A loja Python Toys muda seus preços de acordo com alguns eventos.
Crie um programa que o qual o vendedor informa o preço de um produto. Posteriormente, ele deve perguntar se é uma data festiva.

Caso positivo, insira um acréscimo de 45%.
Caso negativo, mantenha o preço normal. Caso seja Black Friday, insira um desconto de 30% no preço final
'''

rx = 1400
acr = rx + (rx * 0.45)
bf = rx - (rx * 0.3)
print("Olá! Possuímos uma RX 6600 no valor de 1.400,00 Reais!! ")
data = input("Poderia me dizer se estamos prestes a entrar numa data festiva? ")
if data == 'sim':
    print(f"Nessa data ela estará saindo a {acr: .2f} reais. ")
elif data == 'não':
    print(f"O valor se manterá {rx: .2f} reais. ")
elif data == 'black friday':
    print(f"Etará saindo a {bf: .2f} reais com 30% de desconto!! ")