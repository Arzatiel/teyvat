'''
Dado um brinquedo com o valor de 100 reais, peça ao usuáro
que indique se é uma data festiva. Caso positivo, insira um
acréscimo de 40%. Caso negativo, mantenha o preço normal.
Caso seja Black Friday, insira um desconto de 20%. 
'''

toy = 100
pergunta = input("Olá, poderia me dizer se XX dia de XXXX será uma data festiva? Se sim, será black friday?")
if pergunta == 'sim':
    acr = toy + (toy * 0.4)
    print(f"Então nosso brinquedo estará sendo vendido no valor de {acr} reais!")
elif pergunta == 'black friday':
    desc = toy - (toy * 0.2)
    print(f"Estaremos vendendo nosso brinquedo no valor de {desc} reais!")
elif pergunta == 'não':
    print(f"Manteremos nosso brinquedo a {toy} reais.")