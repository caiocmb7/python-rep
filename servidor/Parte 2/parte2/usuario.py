class Usuario:
    def __init__(self, nome, nick, comando, HOST, PORT, status):
        self.nome = nome
        self.nick = nick
        self.comando = comando
        self.HOST = HOST
        self.PORT = PORT
        self.status = status

    def toString(self):
        return self.nome + ', ' + self.nick + ',' + self.comando + ',' + self.PORT + ',' \
        + self.HOST + ',' + self.status


