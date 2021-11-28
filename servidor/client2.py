import sys
import socket
import colorama
import threading

def deleteLastLine():
    # Writes ANSI codes to perform cursor movement and current line clear
    cursorUp = "\x1b[1A"
    eraseLine = "\x1b[2K"
    sys.stdout.write(cursorUp)
    sys.stdout.write(eraseLine)

def send(sock):
    # Handles sending messages to the server
    while threadFlag:
        try:
            message = input()
            deleteLastLine()
            sock.send(message.encode("utf8"))
        except:
            print("Erro durante a mensagem! Possivelmente servidor cheio!")
            break

def receive(sock):
    # Handles receiving messages from the server
    while threadFlag:
        try:
            message = sock.recv(2048).decode()
            if message:
                print("{}".format(message))
            else:
                # When the server closes the socket, messages received are empty
                break
        except:
            print("Erro durante o acesso ao servidor!")
            break

def main():
    # main() will refer to threadFlag as to the global variable defined globally
    global threadFlag

    # Colorama handles the ANSI escape codes to work also on Windows
    colorama.init()
    
    # The host and port of the chat server
    host = "127.0.0.1"
    port = 6789

    # Creates the socket for a TCP application
    socketFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    clientSocket = socket.socket(socketFamily, socketType)

    # Connects to the server
    while True:
        print("Bem vindo a nossa aplicação, esses são seus comandos:")
        print("/ENTRAR para conectar ao server")
        print("/SAIR para sair do server")
        print("/NICKS para mudar seu nick")
        print("/USUARIOS para saber quem esta conectado ao server")

        comando = input("\n Digite seu comando: ")

        if comando == "/ENTRAR":
            host = str(input("Digite o ip do servidor "))
            port = int(input("Digite a porta do servidor:"))
            try:
                clientSocket.connect((host, port))
                break
            except:
                print("O ip ou porta não existe!")
            else:
                break
        else:
            print("Você precisa primeiro entrar no server para usar os outros comandos")

    # Creates two threads for sending and receiving messages from the server
    sendingThread = threading.Thread(target=send, args=(clientSocket,))
    receivingThread = threading.Thread(target=receive, args=(clientSocket,))

    # Start those threads
    receivingThread.start()
    sendingThread.start()

    # Checks if both threads are alive for handling their termination
    while receivingThread.is_alive() and sendingThread.is_alive():
        continue
    threadFlag = False

    # Finally closes the socket object connection
    clientSocket.close()
    print("\nServidor Cheio ou você saiu do chat!")

# Flag used for threads termination
threadFlag = True

if __name__ == "__main__":
    main()
    pass