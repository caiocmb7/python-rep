class Mensagem:
    def __init__(self, nick, msg):
        self.nick = nick
        self.msg = msg

    def toString(self):
        return self.nick + ': ' + self.msg

