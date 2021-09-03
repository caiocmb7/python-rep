class Calculadora:
    def __init__(self):
        pass

    def soma(self, numA, numB):
        return numA + numB
    
    def div(self, numA, numB):
        return numA / numB

    def mul(self, numA, numB):
        return numA * numB

#instanciar o objeto
calculadora = Calculadora()

#nesse caso, nao conseguimos informar no print quem são os valores pq instacia na hora
print(f"\nA soma de é:", calculadora.soma(2, 5))

print(f"\nA multiplicação de é:", calculadora.mul(3, 6))

print(f"\nA divisão de é:", calculadora.div(25, 55))