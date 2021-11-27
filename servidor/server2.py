import atexit
import socket
import threading

def connectionThread(sock):
    # Accepts a connection request and stores both a socket object and its IP address
    while True:
        try:
            client, address = sock.accept()
        except:
            print("Ocorreu um erro com o IP ou Porta do servidor!")
            break
        print("{} conectou-se.".format(address[0]))
        addresses[client] = address
        threading.Thread(target=clientThread, args=(client,)).start()

def clientThread(client):
    # Handles the client
    address = addresses[client][0]
    try:
        message = client.recv(2048).decode("utf8")
        if message == "/ENTRAR":
            user = Nickname(client)
    except:
        print("Ocorreu um erro durante o processo, cheque o nickname ou servidor cheio está cheio! {}!".format(address))
        del addresses[client]
        client.close()
        return
    print("{} entrou com nick de {}!".format(address, user))
    users[client] = user
    
    try:
        client.send("Olá {}! Você conectou-se ao servidor".format(user).encode("utf8"))
    except:
        print("Erro! {} ({}).".format(address, user))
        del addresses[client]
        del users[client]
        client.close()
        return
    broadcast("{} entrou no chat!".format(user))

    # Handles specific messages in a different way (user commands)
    while True:
        try:
            message = client.recv(2048).decode("utf8")
            if message == "/SAIR":
                client.send("Você saiu do chat!".encode("utf8"))
                del addresses[client]
                del users[client]
                client.close()
                print("{} ({}) saiu.".format(address, user))
                broadcast("{} saiu do chat.".format(user))
                break
            elif message == "/USUARIOS":
                lista_usuarios = ', '.join([user for user in sorted(users.values())])
                client.send("Os usuários conectados são: {}".format(lista_usuarios).encode("utf8"))
            elif message == "/NICK":
                client.send("Deseja trocar seu nick para qual?".encode("utf8"))
                new_nickname = client.recv(2048).decode("utf8")
                antigo = users[client]
                users[client] = new_nickname
                user = new_nickname
                print("Nick trocado!")
                broadcast("{} trocou o nick para {}.".format(antigo, users[client]))
            else:
                print("{} ({}): {}".format(address, user, message))
                broadcast(message, user)
        except:
            print("{} ({}) saiu.".format(address, user))
            del addresses[client]
            del users[client]
            client.close()
            broadcast("{} saiu do chat.".format(user))
            break

def Nickname(client):
    # Gets a nickname for a client (if it is not already taken)
    if len(list(users.values())) >= 4:
        print("\nServidor Cheio!")
        client.close()

    client.send("Escolha seu nickname pro chat:".encode("utf8"))
    nickname = client.recv(2048).decode("utf8")
    nick_usado = False
    if nickname in users.values():
        nick_usado = True
        while nick_usado:
            client.send("Esse nick já está sendo usado, tente novamente com outro:".encode("utf8"))
            nickname = client.recv(2048).decode("utf8")
            if nickname not in users.values():
                nick_usado = False
    return nickname

def broadcast(message, sentBy = ""):
    # Broadcasts a message to all users connected
    try:
        if sentBy == "":
            for user in users:
                user.send(message.encode("utf8"))
        else:
            for user in users:
                user.send("{}: {}".format(sentBy, message).encode("utf8"))
    except:
        print("Erro na mensagem!")

def cleanup():
    # Closes all socket object connections
    if len(addresses) != 0:
        for sock in addresses.keys():
            sock.close()
    print("Limpeza feita.")

def main():
    # Register cleanup() as the function to be executed at termination
    atexit.register(cleanup)
    # The host and port for the chat service
    host = "127.0.0.1"
    port = 6789
    # Creates the socket for a TCP application
    socketFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    serverSocket = socket.socket(socketFamily, socketType)
    # Binds the serverSocket at the specified port number
    serverSocket.bind((host, port))
    # Enables accepting connections
    serverSocket.listen()
    # Welcome message to the server owner
    print("Aguardando comandos ...")

    # Creates a thread for accepting incoming connections
    connThread = threading.Thread(target=connectionThread, args=(serverSocket,))
    connThread.start()
    # Waits for it to end
    connThread.join()
    # Performs socket connections cleanup
    cleanup()
    # Closes the server socket object connection
    serverSocket.close()
    print("Server desligado.")

# Dictionaries of nicknames and addresses with socket object as key
users = {}
addresses = {}

if __name__ == "__main__":
    main()
    pass