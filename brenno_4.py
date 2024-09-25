'''
Questão 4

Faça o somatório dos valores a, b, c e divida por d, sem alterar os dados abaixo. O resultado deverá ser
arredondado para ter apenas uma casa decimal.

a = 15
b = 28.0
c = '110'
d = '50.8'
'''

a = 15
b = 28.0
c = '110'
d = '50.8'

soma = (a + b + float(c)) / float(d)
print(f"A soma dos valores é: {soma: .1f} ")