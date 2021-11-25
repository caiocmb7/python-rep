import socket, pickle
from usuario import Usuario
from mensagem import Mensagem

nome = input("\n Qual o seu nome ? ")
comando = input("\n Qual o comando ? ")

if comando == "\entrar":
    PORT = input("\n Digite a porta IP:")
    HOST = input("\n Digite a porta do servidor:")
    Nick = input("\n Digite o nick que voce quer:")

usuario = Usuario(nome, nick, comando, PORT, HOST)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((usuario.HOST, usuario.PORT))
s.sendall(bytes(usuario, 'utf-8'))
status = s.recv(1024).decode('utf-8')

if status == 1 :
    #lógica de envio e recebimento de mensagem
    print("Vc entrou no server")
    while(status):
    msg = input("\n Digite a mensagem:")
    if(msg == "\SAIR"):
        #lógica de sair do servidor
    
    mensagem = Mensagem(usuario.nick,msg)
    data_string = pickle.dumps(mensagem)
    s.sendall(data_string)
    data = s.recv(1024)
    mensagens_recebidas = pickle.loads(data)

s.close()
print ('FROM SERVER: {s}'.format(s=repr(data)))