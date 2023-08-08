# Bem vindo ao Banco Digital Ajr!
# Regras:
# Permitido depositar valores diversos
# Permitido somente 3 saques diários
# Permitido maximo de R$ 500,00 por saque 
# Criação de usuario necessário: Nome, Data de Nascimento, CPF e Endereço
# Não pode cadastrar 2 usuários com o mesmo CPFq


import textwrap

def menu():
    menu = """
    ###### Olá! Seja bem vindo ao Banco AJR! ######
    
    Escolha umas das opções abaixo:
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tAdiconar usúario
    [7]\tSair
    => """

    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

#saque está fora da regra, ainda não aceita somente 3 saques
def sacar(*, saldo, valor_sacado, extrato, limite_valor_saque, numero_de_saques, limite_numero_saques):
    excedeu_saldo = valor_sacado > saldo
    excedeu_limite = valor_sacado > limite_valor_saque
    excedeu_saques = numero_de_saques >= limite_numero_saques

    if excedeu_saldo:
        print("\n### Operação falhou! Você não tem saldo suficiente. ###")

    elif excedeu_limite:
        print("\n### Operação falhou! O valor do saque excede o limite. ###")

    elif excedeu_saques:
        print("\n### Operação falhou! Número máximo de saques excedido. ###")

    elif valor_sacado > 0:
        saldo -= valor_sacado
        extrato += f"Saque:\t\tR$ {valor_sacado:.2f}\n"
        numero_de_saques += 1  
        print("\n=== Saque realizado com sucesso! ===")
        print(f"{numero_de_saques}")
     
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

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
           
            saldo, extrato = sacar(
                saldo = saldo,
                valor_sacado = valor_sacado,
                extrato = extrato,
                limite_valor_saque = limite_valor_saque,
                numero_de_saques = numero_de_saques,
                limite_numero_saques = LIMITE_SAQUES,
            )
            

            
        elif opção == "3":
            #formatação para a saida do valor em "R$ 1500,11"
            print("""\n ================= Extrato =================""")
            print("\n Não foram realizadas movimentações!" if not extrato else extrato)
            print(f"\n Saldo: R$ {saldo:.2f}")
            print("\n ================== FIM ====================")

        elif opção == "4":
            print("\n Obrigado pela visita, até mais! \n")
            break

        else:
            print("\n Operação inválida, por favor selecione novamente a operação desejada. \n")


main()