'''
Questão 6

Em um sistema de aprovação da Universidade Exemplo,
Crie um programa o qual o professor digita a nota do aluno de P1 (primeira prova) e P2
(segunda prova) e fornece a média.
Se a média for igual ou maior que 7, o aluno estará aprovado.
Se for abaixo de 7, não estará aprovado.
Se essa nota de não aprovação for maior ou igual a 3, ele terá uma nova chance, para fazer
uma prova final (P3). A nota abaixo de 3, estará reprovado.
Nessa prova final (p3), é desconsiderado todas as notas anteriores da matéria e o aluno
deverá tirar uma nota maior ou igual a 6 para ser aprovado.
Caso ele ainda não consiga tirar a nota de aprovação na P3 e não tenha tirado uma nota
abaixo ou igual a 3 (que reprovaria na P3), ele poderá fazer uma prova que se chama
Segunda época que é a última chance!
Nessa prova segunda época, o aluno deverá tirar nota maior ou igual a 6 para que seja
aprovado. Se tirar abaixo, estará reprovado!
'''
  
p1 = int(input("Diga sua nota da P1: "))
p2 = int(input("Agora a nota da P2: "))
med =  (p1 + p2) / 2
print(f"Sua média é de {med} pontos. ")
if med >= 7:
    print("Aprovado! ")
elif med < 3:
    print("Reprovado. ")
elif med < 7 and med >= 3:
    print("Não está aprovado, mas terá uma nova chance com a P3. ")
    med1 = int(input("Qual nota você tirou na P3? "))
    if med1 >= 6:
        print("Aprovado!! ")
    elif med1 <= 3:
        print("Reprovado.. ")
    elif med1 == 4 or 5:
        print("é sua última chance, Boa Sorte! ")
        med2 = int(input("Quanto tirou na Segunda Época? "))
        if med2 >= 6:
            print("Finalmente aprovado!!! ")
        else:
            print("Reprovado... ")