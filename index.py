# Bem vindo ao Banco Digital Ajr!
# Regras:
# Permitido depositar valores diversos
# Permitido somente 3 saques diários
# Permitido maximo de R$ 500,00 por saque 
# Criação de usuario necessário: Nome, Data de Nascimento, CPF e Endereço
# Não pode cadastrar 2 usuários com o mesmo CPFq


import textwrap

menu = '''
###### Olá! Seja bem vindo ao Banco AJR! ######

Escolha umas das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
[5] Adiconar usúario
[6] Listar contas
[7] Listar usuarios

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opção = input(menu)

    if opção == "1":
        #numero positivo
        #registro das operações extrato
       
        valor_deposito = float(input("Excelente! Qual o valor para deposito? "))
        
        if valor_deposito > 0:
            print(f"Deposito realizado! O valor de R$ {valor_deposito:.2f} já está disponivel em sua conta!")
            saldo += valor_deposito
            extrato += f"\n Depósito: R$ {valor_deposito:.2f} \n"    

        else:
            print("Por gentileza, rever o valor digitado!")                           
    
    elif opção == "2":
        #tem que ter saldo na conta para poder sacar!
        #limite de 3 saques!
        #limite de 500 por saque!

        valor_sacado = float(input("Excelente! Qual o valor do saque? "))

        excedeu_saldo = valor_sacado > saldo
        excedeu_limite = valor_sacado > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo duficiente!")

        elif excedeu_limite:
            print("\n Operação falhou! O valor do saque exede o seu limite!")
        
        elif excedeu_saques:
            print("\n Operação falhou! Número maximo de saques excedido!")
        
        elif valor_sacado > 0:
            print(f"\n Saque realizado! O valor de R$ {valor_sacado:.2f} foi liberado!")
            saldo -= valor_sacado
            extrato += f"\n Saque: R$ {valor_sacado:.2f} \n"
            numero_saques += 1
        
        else:
            print("Operação falhou, O valor informado é inválido")

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