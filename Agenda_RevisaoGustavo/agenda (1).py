import os

downloads = os.path.join(os.path.expanduser("~"), "Downloads")
caminho_arquivo = os.path.join(downloads, "agenda_contatos.txt")

agenda = []

def inserirContato(agenda):
    valorNome = input("Nome: ")
    valorTelefone = input("Telefone: ")
    valorEmail = input("E-mail: ")
    contato = {
        'nome': valorNome,
        'telefone': valorTelefone,
        'email': valorEmail
    }
    agenda.append(contato)
    print("Contato cadastrado com sucesso!")

def pesquisarPorNome(agenda):
    nome = input("Digite o nome a pesquisar: ")
    for contato in agenda:
        if contato['nome'].upper() == nome.upper():
            print("Contato encontrado:")
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("E-mail:", contato['email'])
            return
    print("Contato não encontrado.")

def pesquisarPorEmail(agenda):
    emailPesquisado = input("Digite o e-mail a pesquisar: ")
    for contato in agenda:
        if contato["email"] == emailPesquisado:
            print("Contato encontrado:")
            print("Nome:", contato['nome'])
            print("Telefone:", contato['telefone'])
            print("E-mail:", contato['email'])
            return
    print("Contato não encontrado.")

def listarTodosOsContatos(agenda):
    if len(agenda) == 0:
        print("A agenda está vazia.")
    else:
        print("Lista de contatos:")
        for contato in agenda:
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("E-mail:", contato["email"])
            print("--------------------")

def gravarAgendaEmArquivo(agenda):
    with open(caminho_arquivo, "w") as arquivo:
        for contato in agenda:
            arquivo.write(f"nome: {contato['nome']}\n")
            arquivo.write(f"telefone: {contato['telefone']}\n")
            arquivo.write(f"email: {contato['email']}\n")
            arquivo.write("--------------------\n")
    print("Agenda de contatos gravada no arquivo 'agenda_contatos.txt'.")

def carregarAgendaDoArquivo(agenda):
    if not os.path.exists(caminho_arquivo):
        print("Arquivo não encontrado.")
        return
    agenda.clear()
    with open(caminho_arquivo, "r") as arquivo:
        contato = {}
        for linha in arquivo:
            if linha.strip() == "--------------------":
                agenda.append(contato)
                contato = {}
            else:
                chave, valor = linha.strip().split(": ", 1)
                contato[chave.lower()] = valor
    print("Agenda carregada com sucesso.")

def mostrarMenu():
    while True:
        print("1 - Inserir contato")
        print("2 - Pesquisar por nome")
        print("3 - Pesquisar por e-mail")
        print("4 - Listar todos os contatos")
        print("5 - Carregar do arquivo")
        print("6 - Gravar em arquivo")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                inserirContato(agenda)
            case "2":
                pesquisarPorNome(agenda)
            case "3":
                pesquisarPorEmail(agenda)
            case "4":
                listarTodosOsContatos(agenda)
            case "5":
                carregarAgendaDoArquivo(agenda)
            case "6":
                gravarAgendaEmArquivo(agenda)
            case "7":
                break
            case _:
                print("Opção inválida. Tente novamente.")

mostrarMenu()
