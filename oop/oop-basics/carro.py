import string
import random 

class Carro:
    def __init__(self, marca, potencia, km_por_litro):
        self.marca = marca
        self.potencia = potencia
        self.km_por_litro = km_por_litro

    def exibirInfo(self):
        print(f"\nA marca do carro é: {self.marca}")
        print(f"\nA potencia do carro é: {self.potencia}")
        print(f"\nA marca do carro é: {self.km_por_litro}")
    
    def definirPlaca(self):
        string.ascii_letters
        l1 = random.choice(string.ascii_letters)
        l2.upper()
        l2 = random.choice(string.ascii_letters)
        l2.upper()
        l3 = random.choice(string.ascii_letters)
        l3.upper()

        n1 = randint(0,9)
        n2 = randint(0,9)
        n3 = randint(0,9)

        placa = l1 + l2 + l3 + "-" + n1 + n2 + n3


