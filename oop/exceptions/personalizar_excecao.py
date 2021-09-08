class Erro(Exception):
    pass

class InputError(Erro):
    def __init__(self, message):
        self.message = message

while True:      
    try:
        x = int(input("Digite um valor inteiro entre 0 e 10: "))
        print(x)
        if x > 10:
            raise InputError("Valor ACIMA de 10, digite um valor somente no range pedido")
        elif x < 10: 
            raise InputError("Valor ABAIXO de 0, digite uma valor somente no range pedido")
        break
    except ValueError:
        print("Por favor digite apenas um valor inteiro")
