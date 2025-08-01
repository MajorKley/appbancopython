numero_conta = 0
saldo = 0
deposito = 0
saque = 0



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

def saldo_conta(saque):
    global saldo
    if saque <= saldo:
        saldo -= saque 
        print(f'Saque de R${saque} foi realizado com sucesso. Novo saldo: R${saldo}')
    else:
        print("Saldo insuficiente!")
        return

def deposito_conta (deposito):
    global saldo
    saldo += deposito
    print(f'Deposito de R${deposito} foi realizado com sucesso. Novo saldo: R${saldo}')
    




usuario = None
conta = None



#MENU
while True:

    print("------------- Menu --------------"
            "\n Opção 01: Já tenho uma conta"
            "\n Opção 02: Criar conta"
            "\n Opcao 03: Sair")
    
    opcao = input("Digite a opção do seu atendimento: ")

    if opcao == "1":
        
        if usuario is None or conta is None:
            print("Nenhuma conta cadastrada. Crie sua conta primeiro")
            continue

        login_nome = input("Digite seu nome: ")
        login_agencia = input("Digite sua agência: ")
        login_numero_conta = input("Digite o número da sua conta:")

        if login_nome == usuario[0] and login_agencia == conta[1] and int(login_numero_conta) == conta[0]:

            while True:
                print(
                "------------- Menu Bancário --------------"
                "\n Servico 01: Saque"
                "\n Servico 02: Depósito"
                "\n Servico 03: Extrato"
                "\n Servico 04: Sair")


                servico = input("Digite o serviço que deseja: ")

                if servico == "1":
                    saque = int(input("Quanto gostaria de sacar? "))
                    saldo_conta(saque)
                    

                
                elif servico == "2":
                    deposito = int(input("Qual o valor que será depositado?"))
                    deposito_conta(deposito)
                    
                elif servico == "3":
                    print("----Extrato-----")
                    print(f'Saldo: {saldo}')
                    print(f'Deposito: {deposito}')
                    print(f'Saque: {saque}')
                
                elif servico == "4":
                    break   

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
        
    elif opcao == "3":
        break

    else:
        print ("Escolha uma opção válida")
        



       
   