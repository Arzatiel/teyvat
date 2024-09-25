'''
Questão 7

Em Porto Velho, Rondônia temos um campeonato de um jogo muito famoso. Mas este, tem algumas regras
para que ocorra ou não. Este jogo ocorre em anos que são divisíveis por 4, mas que não seja divisível por
100, a não ser que também seja divisível por 400.
Se for ano de campeonato, deverá aparecer a mensagem : Este é um ano de campeonato .
Se não for, deverá imprimir a mensagem: Este não é um ano de campeonato
'''

ano = int(input("Diga um ano: "))
if ano % 400 != 0 and ano % 100 == 0:
    print("Este ano não terá campeonato! ")
elif ano % 4 > 0:
    print("Este ano não teremos campeonato! ")
elif ano % 4 == 0:
    print("Este ano teremos campeonato. ")