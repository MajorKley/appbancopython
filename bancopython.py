numero_conta = 0


def cadastro_usuario():
#Infos Clientes
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira a data de nascimento: ")
    cpf = input("Insira o CPF: ")
        #endereco
    endereco = [input("Digite o logradouro: "),
                input("Digite o número: "),
                input("Digite o Bairro: "),
                input("Digite a UF: ")]
    return [nome, data_nascimento, cpf, endereco]



def criacao_conta():
    global numero_conta
    numero_conta += 1
    agencia = "0001"

    return [numero_conta, agencia]


usuario = None
conta = None

#MENU
while True:

    print("------------- Menu Bancário --------------"
            "\n Opção 01: Já tenho uma conta"
            "\n Opção 02: Criar conta")
    
    opcao = input("Digite a opção do seu atendimento: ")

    if opcao == "1":
        
        if usuario is None or conta is None:
            print("Nenhuma conta cadastrada. Crie sua conta primeiro")
            continue

        login_nome = input("Digite seu nome: ")
        login_agencia = input("Digite sua agência: ")
        login_numero_conta = input("Digite o número da sua conta:")

        if login_nome == usuario[0] and login_agencia == conta[1] and int(login_numero_conta) == conta[0]:

            print(
            "------------- Menu Bancário --------------"
            "\n Servico 01: Saque"
            "\n Servico 02: Depósito"
            "\n Servico 03: Extrato")

            servico = input("Digite o serviço que deseja: ")

            if servico == "1":
                print("saque")
            
            elif servico == "2":
                print ("deposito")
            
            elif servico == "3":
                print("extrato")

            else:
                print("Escolha um serviço válido")
            
        else:
            print("Dados inválidos")

        
    elif opcao == "2":
        print("--------Criação de conta--------")
        usuario = cadastro_usuario()
        conta = criacao_conta()


        print(f"\nParabéns, {usuario[0]}!")
        print(f"Sua conta é {conta[0]}.")
        print(f"Sua Agência é {conta[1]}.")
        
         
    else:
        print ("Escolha uma opção válida")
        break



       
   