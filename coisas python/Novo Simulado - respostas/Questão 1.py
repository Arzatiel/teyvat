'''
Crie um programa que, pergunte ao usuário como ele está.
Se ele estiver bem, responda: Que bom!
Se ele estiver mal, pergunte por qual motivo. Quando ele
responder, responda que lamenta. 
'''

print("Olá, seja Bem-vindo(a)")
estado = input("Como você está? ")
if estado == 'bem':
    print("Que Bom!")
else:
    input("Por qual motivo?")
    print("Lamento...")