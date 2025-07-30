def cadastro_usuario():
#Infos Clientes
    print("Cadastro Clientes")
    nome = input("Insira seu nome:")
    data_nascimento = input("Insira a data de nascimento:")
    cpf = input("Insira o CPF:")
        #endereco
    endereco = [input("Digite o logradouro:"),
                input("Digite o número:"),
                input("Digite o Bairro:"),
                input("Digite a UF:")]



#MENU
while True:

    print("------------- Menu Bancário --------------"
            "\n Opção 01: Já tenho uma conta"
            "\n Opção 02: Criar conta")
    
    opcao = input("Digite a opção do seu atendimento")

    if opcao == "1":
    
        print(
        "------------- Menu Bancário --------------"
        "\n Servico 01: Saque"
        "\n Servico 02: Depósito"
        "\n Servico 03: Extrato")

        servico = input("Digite o serviço que deseja:")

        if servico == "1":
            print = ("saque")
        
        elif servico == "2":
            print = ("deposito")
        
        if servico == "3":
            print = ("extrato")

        else:
            print("Escolha um serviço válido")
        break
    
    elif opcao == "2":
        cadastro_usuario()
    
    else:
        print ("Escolha uma opção válida")
        break
   