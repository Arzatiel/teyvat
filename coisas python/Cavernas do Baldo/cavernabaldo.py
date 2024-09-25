import os
import random
import pygame, sys, time

pygame.mixer.init()

def prompt():
    print("\t\t\tBem vindo às Cavernas do Baldo.\n\n\
Você deve recolher todos os 6 itens antes de lutar contra o temível Killer Bean.\n\n\
Dica: É recomendável que o jogador lembre ou anote as salas em que já esteve para conseguir pegar todos os itens.\n\n\
Movimentos:\t'Ir {direcao}'(ir norte, sul, leste, oeste. Ex: 'ir norte')\n\
\t'Pegar {item}'(adicionar itens próximos ao inventário. Ex: 'pegar amuleto de prontera')\n")
    
    input('Pressione enter para continuar...')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



salas = {
    'Entrada': {'Norte': 'Cripta Subterranea', 'Sul': 'Acampamento Abandonado', 'Leste': 'Loja Misteriosa'},
    'Cripta Subterranea': {'Sul': 'Entrada', 'Item': 'Frasco De Estus'},
    'Acampamento Abandonado': {'Norte': 'Entrada', 'Leste': 'Mina Abandonada', 'Item': 'Amuleto De Prontera'},
    'Mina Abandonada': {'Oeste': 'Acampamento Abandonado', 'Item': 'Armadura De Diamante Encantada'},
    'Loja Misteriosa': {'Norte': 'Portão do Baldo', 'Leste': 'Sala do Killer Bean', 'Oeste': 'Entrada', 'Item': 'Chave Do Baldo'},
    'Sala do Killer Bean': {'Oeste': 'Loja Misteriosa', 'Boss': 'Killer Bean'},
    'Portão do Baldo': {'Sul': 'Loja Misteriosa', 'Leste': 'Sala da Estrela de Safira', 'Item': 'Divine Bone Shard'},
    'Sala da Estrela de Safira': {'Oeste': 'Portão do Baldo', 'Item': 'Emblema Do Heroi'}
    }


inventario = []

sala_atual = 'Entrada'

msg = ''

mensagem_derrota = ['Você foi obliterado pelo ', 'Você foi massacrado pelo ',
                    'Você foi feito de gato e sapato pelo ', 'Você foi atropelado pelo ',
                    'Você foi esfaqueado pelo ', 'Você foi derrotado pelo ']

clear()
prompt()


while True:
    pygame.mixer.music.load('fungalfunk.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.1)
    while True:

        clear()

        print(f"Você está na(o) {sala_atual}\nInventário: {inventario}\n{'-' * 27}")
        print(msg)


        if 'Item' in salas[sala_atual].keys():

            item_proximo = salas[sala_atual]['Item']

            if item_proximo not in inventario:

                print(f'Você vê um(a) {item_proximo}')

        if 'Boss' in salas[sala_atual].keys():

            if len(inventario) < 6:
                print(random.choice(mensagem_derrota))
                print(f"{salas[sala_atual]['Boss']}.")
                sys.exit()
            
            else:
                print(f"Parabéns, você venceu o poderoso {salas[sala_atual]['Boss']}!!!")
                pygame.mixer.music.unload()
                pygame.mixer.music.load('vitoria.mp3')
                pygame.mixer.music.play()
                input('Pressione enter para sair...')
                sys.exit()
        
        input_usuario = input('Insira seu movimento:\n')
        proximo_movimento = input_usuario.split(' ')
        action = proximo_movimento[0].title()

        if len(proximo_movimento) > 1:
            item = proximo_movimento[1:]
            direcao = proximo_movimento[1].title()

            item = ' '.join(item).title()
        
        if action == "Ir":

            try:
                sala_atual = salas[sala_atual][direcao]
                msg = f'Você vai para {direcao}'

            except:
                msg = f'Você não pode fazer esse movimento.'

        elif action == 'Pegar':      
            try:
                if item == salas[sala_atual]['Item']:            
                    if item not in inventario:
                        inventario.append(salas[sala_atual]['Item'])
                        msg = f'{item} foi adquirido!'
                    else:
                        msg = f'Você já tem {item} no seu inventário.'   

                else:
                    msg = f'Você não encontrou {item}.'

            except:
                msg = f'Você não encontrou {item}.'    

        elif action == 'Sair':
            break

        else:
            msg = 'Comando Inválido'
