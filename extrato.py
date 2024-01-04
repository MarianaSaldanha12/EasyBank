import sqlite3

class Extrato:
    def __init__(self):
        self.conexao = sqlite3.connect('Easy_Bank.sqlite')
        self.cursor = self.conexao.cursor()

        # Restante da lógica da classe Extrato

    def salvar_extrato(self, transacoes):
        for transacao in transacoes:
            self.cursor.execute('''
                INSERT INTO transacoes (descricao, valor)
                VALUES (?, ?)
            ''', (transacao,))  # Aqui supõe-se que o valor seria alguma variável numérica da transação
        self.conexao.commit()
        print("Extrato salvo com sucesso!")

    def carregar_extrato(self):
        self.cursor.execute('''
            SELECT descricao FROM transacoes
        ''')
        extrato = self.cursor.fetchall()
        return [row[0] for row in extrato]

    def apagar_extrato(self):
        self.cursor.execute('''
            DELETE FROM transacoes
        ''')
        self.conexao.commit()
        print("Extrato apagado com sucesso!")

