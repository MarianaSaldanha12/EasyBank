import sqlite3
import getpass

class Clientes:
    def __init__(self):
        self.conexao = sqlite3.connect('Easy_Bank.sqlite')
        self.cursor = self.conexao.cursor()
        self.conta_criada = False  # Adicionando o atributo conta_criada

    def criar_conta(self):
        if not self.conta_criada:
            # Coletar dados da conta
            self.nome = input("Digite seu nome: ")
            self.email = input("Digite seu email: ")
            self.cpf = input("Digite seu CPF: ")
            self.data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
            
            # Definir credenciais
            self.usuario = input("Digite o nome de usuário desejado: ")
            self.senha = getpass.getpass("Digite a senha desejada: ")
            
            # Inserir dados na tabela clientes
            self.cursor.execute('''
                INSERT INTO clientes (nome, email, cpf, data_nascimento, usuario, senha)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.nome, self.email, self.cpf, self.data_nascimento, self.usuario, self.senha))
            self.conexao.commit()
            
            self.conta_criada = True
            print("Conta criada com sucesso!")
        else:
            print("Conta já foi criada!")

    def autenticar(self):
        if not self.conta_criada:
            print("Crie uma conta antes de fazer login.")
            return False

        tentativas = 3
        while tentativas > 0:
            usuario_input = input("Usuário: ")
            senha_input = getpass.getpass("Senha: ")

            self.cursor.execute('''
                SELECT usuario, senha FROM clientes WHERE usuario = ? AND senha = ?
            ''', (usuario_input, senha_input))
            resultado = self.cursor.fetchone()

            if resultado:
                print("Login bem-sucedido!")
                return True
            else:
                tentativas -= 1
                print(f"Credenciais incorretas. Tentativas restantes: {tentativas}")
        
        print("Número de tentativas excedido. Tente novamente mais tarde.")
        return False

    def coletar_dados_conta(self):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        cpf = input("Digite seu CPF: ")
        data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

        return nome, email, cpf, data_nascimento

    def sacar(self):
        if not self.conta_criada:
            print("Crie uma conta antes de realizar outras operações.")
            return
        valor = float(input("Informe a quantia para o saque: "))
        self.saldo -= valor  # Atualizando o saldo após o saque
        transacao = f"Saque: - R$ {valor:.2f}"
        self.extrato.salvar_extrato(self.extrato.carregar_extrato() + [transacao])
        print(f"Saque de R$ {valor:.2f} efetuado com sucesso.")
        print(f"Saldo restante: R$ {self.saldo:.2f}")
    def depositar(self):
        if not self.conta_criada:
            print("Crie uma conta antes de realizar outras operações.")
            return
        valor = float(input("Informe a quantia para o depósito: "))
        self.saldo += valor  # Atualizando o saldo após o depósito
        transacao = f"Depósito: + R$ {valor:.2f}"
        self.extrato.salvar_extrato(self.extrato.carregar_extrato() + [transacao])
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("Exibindo o extrato...")
    def exibir_extrato(self):
        if not self.conta_criada:
            print("Crie uma conta antes de realizar outras operações.")
            return
        print("Exibindo o extrato...")
        extrato = self.extrato.carregar_extrato()
        if len(extrato) == 0:
            print("Nenhuma transação no extrato")
        else:
            for transacao in extrato:
                print(transacao.strip())  # Remove quebras de linha ao imprimir
    def excluir_conta(self):
        self.extrato.apagar_extrato()  # Chama a função para apagar o extrato
        self.saldo = 0.0  # Reinicia o saldo para zero
        self.conta_criada = False
        print("Conta excluída com sucesso!")