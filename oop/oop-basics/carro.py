import string
import random 
from random import randint

class Carro:
    def __init__(self, marca, potencia, km_por_litro):
        self.marca = marca
        self.potencia = potencia
        self.km_por_litro = km_por_litro


    def exibirInfo(self):
        print(f"\nA marca do carro é: {self.marca}")
        print(f"\nA potencia do carro é: {self.potencia}")
        print(f"\nO carro faz: {self.km_por_litro}")
    
    def definirPlaca(self):
        l1 = random.choice(string.ascii_letters).upper()
        l2 = random.choice(string.ascii_letters).upper()
        l3 = random.choice(string.ascii_letters).upper()

        n1 = str(randint(0,9))
        n2 = str(randint(0,9))
        n3 = str(randint(0,9))

        placa = l1 + l2 + l3 + "-" + n1 + n2 + n3
        return f"\nA placa do carro será: {placa}"
    
    def definirCor(self):
        lista = ['Rosa', 'Amarelo', 'Azul', 'Preto', 'Branco', 'Cinza', 'Verde', 'Roxo', 'Marrom']
        chute = random.choice(lista)
        return f"\nA cor do carro será: {chute}"

class carro_automobilismo(Carro):
    def __init__(self, marca, potencia, km_por_litro, tamanho):
        self.tamanho = tamanho
        super().__init__(marca, potencia / 10, km_por_litro)  




carro_teste = Carro('Toyota', 1200, '10 km/L')

carro_teste_automobilismo = carro_automobilismo('KIA', 120, '5 km/L', 'pequeno')
print(carro_teste.exibirInfo())
print(carro_teste.definirPlaca())
print(carro_teste.definirCor())
print(carro_teste_automobilismo.definirCor())
print(carro_teste_automobilismo.exibirInfo())
print(carro_teste_automobilismo.tamanho)


