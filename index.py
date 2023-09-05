# Bem vindo ao Banco Digital Ajr!
# Regras:
# Permitido depositar valores diversos
# Permitido somente 3 saques diários
# Permitido maximo de R$ 500,00 por saque 
# Cadastro de conta
# Cadastro de usuario - Necessário: Nome, Data de Nascimento, CPF e Endereço
# Cadastro de 2 usuários com o mesmo CPF

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
























