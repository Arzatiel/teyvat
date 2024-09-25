'''
Questão 2

Um atacadista quer inserir um desconto de 40% em todos os produtos em uma promoção relampago! Crie
um programa onde o usuário digita o nome de um produto e o seu preço. Ao Lnal será mostrado a
mensagem informando:
Exemplo: A bola vai custar 16 reais com 40% de desconto
'''

print("Bem vindo!!")
brinq = input("Diga o nome de um produto e lhe informaremos o seu valor com desconto: ")
val = float(input("E a que valor ele se encontra? "))
val1 = val - (val * 0.4)
print(f"O produto {brinq} vai custar {val1: .2f} com 40% de desconto!")