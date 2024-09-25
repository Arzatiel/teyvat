
# clientes = []

# def adicionar_cliente(nome, email, tel, end):
#     cliente = [nome, email, tel, end]
#     clientes.append(cliente)
#     print(f'Cliente {nome} adicionado!')

# def exibir_clientes():
#         for cliente in clientes:
#             print(f'\nNome: {cliente[0]}.\nEmail: {cliente[1]}.\nTelefone: {cliente[2]}.\nEndereço: {cliente[3]}. ')

# def buscar_email(email):
#     cliente_enc = False
#     for cliente in clientes:
#         if cliente[1] == email:
#             print(f'Cliente encontrado: \nNome: {cliente[0]}\nE-mail: {cliente[1]}\nTelefone: {cliente[2]}\nEndereço: {cliente[3]}')
#             cliente_enc = True
#     if not cliente_enc:
#         print('Cliente não encontrado. ')

# def remover_cliente(email):
#     cliente_enc = False
#     for i, cliente in enumerate(clientes):
#         if cliente[1] == email:
#             clientes.remove(cliente)
#             print(f'Cliente com {email} removido com sucesso!')
#             cliente_enc = True
#     if not cliente_enc:
#         print('Cliente não encontrado. ')

# def infos():
#     while True:
#         print('Escolha uma opção a seguir: \n0 - Adicionar Cliente. \n1 - Mostrar Cliente. \n2 - Procurar Cliente. \n3 - Remover Cliente. \n4 - Sair. ')
#         opções = input('Opção: ')
#         if opções == '0':
#             nome = input('Digite o nome do cliente: ')
#             email = input('Digite o email do cliente: ')
#             end = input('Digite o telefone do cliente: ')
#             tel = input('Digite o endereço do cliete: ')
#             adicionar_cliente(nome, email, end, tel)
#         elif opções == '1':
#             exibir_clientes()
#         elif opções == '2':
#             email = input('Digite o email do cliente: ')
#             buscar_email(email)
#             esc = input('Digite (1) para continuar ou (2) para sair. ')
#             if esc == '1':
#                 continue
#             elif esc == '2':
#                 break
#         elif opções == '3':
#             email = input('Digite o email do cliente: ')
#             remover_cliente(email)
#             esc = input('Digite (1) para continuar ou (2) para sair. ')
#             if esc == '1':
#                 continue
#             elif esc == '2':
#                 break

#         elif opções == '4':
#             print('Até mais! ')
#             break
#         else:
#             print('Escolha uma opção válida! ')

# infos()
# Lista para armazenar as entregas
entregas = []

# Função para cadastrar uma nova entrega
def cadastrar_entrega(codigo, fornecedor, cliente, destino, status):
    entrega = {
        'codigo': codigo,
        'fornecedor': fornecedor,
        'cliente': cliente,
        'destino': destino,
        'status': status
    }
    entregas.append(entrega)
    print(f"Entrega {codigo} cadastrada com sucesso.")

# Função para atualizar o status de uma entrega pelo código
def atualizar_status(codigo, novo_status):
    for entrega in entregas:
        if entrega['codigo'] == codigo:
            entrega['status'] = novo_status
            print(f"Status da entrega {codigo} atualizado para '{novo_status}'.")
            return
    print("Entrega não encontrada.")

# Função para buscar uma entrega pelo código
def buscar_entrega(codigo):
    for entrega in entregas:
        if entrega['codigo'] == codigo:
            return entrega
    return None

# Função para listar todas as entregas
def listar_entregas():
    if not entregas:
        print("Não há entregas disponíveis.")
    else:
        for entrega in entregas:
            print(f"Código: {entrega['codigo']}, Fornecedor: {entrega['fornecedor']}, Cliente: {entrega['cliente']}, Destino: {entrega['destino']}, Status: {entrega['status']}")

# Função para contar o número de entregas de um fornecedor específico
def contar_entregas_por_fornecedor(fornecedor):
    contagem = 0
    for entrega in entregas:
        if entrega['fornecedor'] == fornecedor:
            contagem += 1
    print(f"O fornecedor '{fornecedor}' tem {contagem} entrega(s) cadastrada(s).")

# Função auxiliar para gerar código no formato "E001", "E002", etc.
def gerar_codigo_entrega():
    return f"E{len(entregas) + 1:03d}"

# Exemplo de uso do sistema
while True:
    print("\n--- Sistema de Gestão de Entregas ---")
    print("1. Cadastrar Entrega")
    print("2. Atualizar Status de Entrega")
    print("3. Buscar Entrega por Código")
    print("4. Listar Todas as Entregas")
    print("5. Contar Entregas por Fornecedor")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        fornecedor = input("Nome do fornecedor: ")
        cliente = input("Nome do cliente: ")
        destino = input("Endereço de destino: ")
        status = input("Status inicial da entrega (Pendente, Em Transito, Entregue): ")
        codigo = gerar_codigo_entrega()
        cadastrar_entrega(codigo, fornecedor, cliente, destino, status)

    elif opcao == '2':
        codigo = input("Código da entrega: ")
        novo_status = input("Novo status (Pendente, Em Transito, Entregue): ")
        atualizar_status(codigo, novo_status)

    elif opcao == '3':
        codigo = input("Código da entrega: ")
        entrega = buscar_entrega(codigo)
        if entrega:
            print(f"Código: {entrega['codigo']}, Fornecedor: {entrega['fornecedor']}, Cliente: {entrega['cliente']}, Destino: {entrega['destino']}, Status: {entrega['status']}")
        else:
            print("Entrega não encontrada.")

    elif opcao == '4':
        listar_entregas()

    elif opcao == '5':
        fornecedor = input("Nome do fornecedor: ")
        contar_entregas_por_fornecedor(fornecedor)

    elif opcao == '6':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
