'''
Crie um programa que simule uma batalha com uma rolagem de
dados, com um dado de 10 lados. Se o número der maior que
7, indica que você acertou o golpe.
'''
# coloquei 20 pra combinar mais com D&D.

import random
dado = random.randint(1, 20)
if dado == 1:
    print(f"VOCê TIROU {dado} NO DADO E OBTEVE UM ERRO CRÍTICO!!!")
elif dado == 20:
    print(f"VOCÊ TIROU {dado} NO DADO E OBTEVE UM ACERTO CRÍTICO!!!")
elif dado >= 7:
    print(f"A rolagem de dados deu {dado} e você acertou o golpe!")
elif dado <= 6:
    print(f"Você tirou {dado} na rolagem e errou o golpe!")