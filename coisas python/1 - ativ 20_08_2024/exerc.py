
clientes = []

def adicionar_cliente(nome, email, tel, end):
    cliente = [nome, email, tel, end]
    clientes.append(cliente)
    print(f'Cliente {nome} adicionado!')

def exibir_clientes():
        for cliente in clientes:
            print(f'\nNome: {cliente[0]}.\nEmail: {cliente[1]}.\nTelefone: {cliente[2]}.\nEndereço: {cliente[3]}. ')

def buscar_email(email):
    cliente_enc = False
    for cliente in clientes:
        if cliente[1] == email:
            print(f'Cliente encontrado: \nNome: {cliente[0]}\nE-mail: {cliente[1]}\nTelefone: {cliente[2]}\nEndereço: {cliente[3]}')
            cliente_enc = True
    if not cliente_enc:
        print('Cliente não encontrado. ')

def remover_cliente(email):
    cliente_enc = False
    for i, cliente in enumerate(clientes):
        if cliente[1] == email:
            clientes.remove(cliente)
            print(f'Cliente com {email} removido com sucesso!')
            cliente_enc = True
    if not cliente_enc:
        print('Cliente não encontrado. ')

def infos():
    while True:
        print('Escolha uma opção a seguir: \n0 - Adicionar Cliente. \n1 - Mostrar Cliente. \n2 - Procurar Cliente. \n3 - Remover Cliente. \n4 - Sair. ')
        opções = input('Opção: ')
        if opções == '0':
            nome = input('Digite o nome do cliente: ')
            email = input('Digite o email do cliente: ')
            end = input('Digite o telefone do cliente: ')
            tel = input('Digite o endereço do cliete: ')
            adicionar_cliente(nome, email, end, tel)
        elif opções == '1':
            exibir_clientes()
        elif opções == '2':
            email = input('Digite o email do cliente: ')
            buscar_email(email)
            esc = input('Digite (1) para continuar ou (2) para sair. ')
            if esc == '1':
                continue
            elif esc == '2':
                break
        elif opções == '3':
            email = input('Digite o email do cliente: ')
            remover_cliente(email)
            esc = input('Digite (1) para continuar ou (2) para sair. ')
            if esc == '1':
                continue
            elif esc == '2':
                break

        elif opções == '4':
            print('Até mais! ')
            break
        else:
            print('Escolha uma opção válida! ')

infos()

