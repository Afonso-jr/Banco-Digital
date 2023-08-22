# Bem vindo ao Banco Digital Ajr!
# Regras:
# Permitido depositar valores diversos
# Permitido somente 3 saques diários
# Permitido maximo de R$ 500,00 por saque 
# Cadastro de conta
# Cadastro de usuario - Necessário: Nome, Data de Nascimento, CPF e Endereço
# É possivel cadastrar 1 Usuário por CPF
# É possivel cadastrar varias contas usando o mesmo CPF

import textwrap

def menu():
    menu = """
    ###### Olá! Seja bem vindo ao Banco AJR! ######
    
    Escolha umas das opções abaixo:
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tAdiconar usúario
    [5]\tNova conta
    [6]\tListar contas
    [7]\tSair
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\t\tR$ {valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

def sacar(*, saldo, valor_sacado, extrato, limite_valor_saque, numero_de_saques, limite_numero_saques):
    excedeu_saldo = valor_sacado > saldo
    excedeu_limite = valor_sacado > limite_valor_saque
    excedeu_saques = numero_de_saques >= limite_numero_saques

    if excedeu_saldo:
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")

    elif excedeu_limite:
        print("\n### Operação falhou! O valor do saque excede o limite. ###")

    elif excedeu_saques:
        print("\n### Operação falhou! Número máximo de 3 saques diários excedido. ###")

    elif valor_sacado > 0:
        saldo -= valor_sacado
        extrato += f"Saque:\t\t\tR$ {valor_sacado:.2f}\n"
        numero_de_saques += 1  
        print(f"\n=== O valor de R$ {valor_sacado:.2f} já pode ser sacado! ===")
         
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato, numero_de_saques

def exibir_extrato(saldo, /, *, extrato):
    #formatação para a saida do valor em "R$ 1500,11"
            print("""\n ================= Extrato =================""")
            print("\n Não foram realizadas movimentações!" if not extrato else extrato)
            print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
            print("\n ================== FIM ====================")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### Já existe usuário com esse CPF! ###")
        return 
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento *somente o numero (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###")

def listar_contas(contas):
    if contas == []:
        print("\n### Ainda não foram criadas nenhuma conta! ###")
    else:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_valor_saque = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opção = menu()

        if opção == "1":
            #numero positivo
            #registro das operações extrato
            valor_deposito = float(input("Excelente! Qual o valor para deposito? "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)                     
        
        elif opção == "2":
            #tem que ter saldo na conta para poder sacar!
            #limite de 3 saques!
            #limite de 500 por saque!

            valor_sacado = float(input("Excelente! Qual o valor do saque? "))
           
            saldo, extrato, numero_de_saques = sacar(
                saldo = saldo,
                valor_sacado = valor_sacado,
                extrato = extrato,
                limite_valor_saque = limite_valor_saque,
                numero_de_saques = numero_de_saques,
                limite_numero_saques = LIMITE_SAQUES,
            )            

        elif opção == "3":
            exibir_extrato(saldo, extrato = extrato)
        
        elif opção == "4":
            novo_usuario(usuarios)
        
        elif opção == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opção == "6":
            listar_contas(contas)
        
        elif opção == "7":
            print("\n Obrigado pela visita, até mais! \n")
            break

        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada. \n")

main()