import socket

# setup

host = ""
port = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

# controle server-client

while True:
    print("Aguardando nova mensagem...\n")
    op, local = s.recvfrom(1024)
    resp = str(eval(op))
    print("----- Resposta da Calculadora -----\n")
    print(f"Resposta realizada na calculadora: {resp}\n")
    print("----- Cálculo realizado -----\n")

    s.sendto(bytes(resp, "utf-8"), local) # manda de volta pro client