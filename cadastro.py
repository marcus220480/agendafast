import re

def menu():
    while True:
        opcao = input('''
    ___________________________________________
                        CONTATOS
    LISTA
    [1]CADASTRAR
    [2]LISTAR
    [3]DELETAR
    [4]BUSCAR
    [5]EXIT
    ____________________________________________ 
    SELECIONE A OPÇÃO NUMÉRICA:
    ''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloNome()
        elif opcao == "5":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

        voltar_menu = input("Voltar ao menu principal? (y/n): ").lower()
        if voltar_menu != 'y':
            break

def gerar_id():
    try:
        with open("cadastro.txt", "r") as cadastro:
            linhas = cadastro.readlines()
            if linhas:
                ultimo_id = int(linhas[-1].split(";")[0])
                return ultimo_id + 1
            else:
                return 1
    except FileNotFoundError:
        return 1

def validar_telefone(telefone):
    padrao = r"^\(\d{2}\)\d{4}-\d{4}$"
    if re.match(padrao, telefone):
        return True
    else:
        return False

def cadastrarContato():
    id_contato = gerar_id()
    nome = input("Nome do contato: ")

    while True:
        telefone = input("Telefone do contato (formato: (00)0000-0000): ")
        if validar_telefone(telefone):
            break
        else:
            print("Formato de telefone inválido. Tente novamente.")

    email = input("Email do contato: ")

    try:
        with open("cadastro.txt", "a") as cadastro:
            dados = f'{id_contato};{nome};{telefone};{email}\n'
            cadastro.write(dados)
            print('Contato gravado!')
    except IOError:
        print("Erro ao gravar o contato.")

def listarContato():
    try:
        with open("cadastro.txt", "r") as cadastro:
            contatos = cadastro.readlines()
            if contatos:
                for contato in contatos:
                    print(contato.strip())
            else:
                print("Nenhum contato encontrado.")
    except FileNotFoundError:
        print("Arquivo de cadastro não encontrado.")

def deletarContato():
    nome_deletado = input("Digite o nome: ")
    try:
        with open("cadastro.txt", "r") as cadastro:
            contatos = cadastro.readlines()

        contatos_atualizados = [contato for contato in contatos if nome_deletado not in contato.split(";")[1]]
        
        with open("cadastro.txt", "w") as cadastro:
            cadastro.writelines(contatos_atualizados)
        
        if len(contatos) != len(contatos_atualizados):
            print(f'Contato deletado.')
            listar_contatos()
        else:
            print("Contato não encontrado.")
    except FileNotFoundError:
        print("Arquivo de cadastro não encontrado.")

def buscarContatoPeloNome():
    nome = input('Digite o nome: ').upper()
    try:
        with open("cadastro.txt", "r") as cadastro:
            contatos = [contato for contato in cadastro if nome in contato.split(";")[1].upper()]
            if contatos:
                for contato in contatos:
                    print(contato.strip())
            else:
                print("Contato não encontrado.")
    except FileNotFoundError:
        print("Arquivo de cadastro não encontrado.")

def sair():
    print('Obrigado!')
    exit()

menu()
