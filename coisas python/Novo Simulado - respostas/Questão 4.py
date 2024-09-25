'''
Escreva um programa em Python que calcule o valor futuro de
um investimento com base na taxa de juros anual, no tempo
de investimento e no valor inicial investido. O programa
deve usar a fórmula de juros compostos:

Formula:
Valor Futuro = Valor Inicial * (1 + Taxa de Juros/100)^Tempo

Deverá ter o valor inicial de investimento
Taxa de juros
Quantidade de anos
'''

juros = 10
vi = float(input("Qual o valor de investimento? "))
tempo = float(input("Por quantos anos seria este investimento? "))
vf = vi * (1 + juros / 100) ** tempo
print(f"O valor futuro desse investimento será de {vf:.2f} reais.")
