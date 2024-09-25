'''Crie um programa que:
Dado um inteiro, realize as seguintes ações condicionais:
EX 1: Se  for ímpar, imprima Estranho
EX 2: Se  for par e estiver no intervalo inclusivo de 2 a 5, imprima Não Estranho
EX 3: Se  for par e estiver no intervalo inclusivo de 6 a 20, imprima Estranho
EX 4: Se  for par e maior que 20, imprima Não Estranho'''

# RETIRE AS ASPAS TRIPLAS NO COMEÇO E NO FIM DO CODIGO DE CADA EXERCÍCIO PARA O TESTE.

# EXERCÍCIO 1: #

'''
while True:
    try:
        num = int(input("Escolha um número para identificar se é Par ou Ímpar:"))
        resultado = num % 2
    except ValueError:
        print("Por favor, escolha um número válido.")
        continue
    if resultado == 0:
        print("Este é um número par.")
        break
    else:
        print("Este é um número ímpar.")
        break
'''

####################################################################################

# EXERCÍCIO 2: #

