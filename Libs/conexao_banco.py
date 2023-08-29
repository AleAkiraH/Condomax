import sqlite3


class ConexaoBanco:
    def __init__(self):
        self.conn = sqlite3.connect('Condomax')
        self.cursor = self.conn.cursor()

    def fechar_conexao(self):
        self.conn.close()
