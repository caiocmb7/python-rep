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

print("\nA soma de {numA} + {numB} é: ", calculadora.soma(5, 5))

print("\nA soma de {numA} * {numB} é: ", calculadora.mul(5, 5))

print("\nA soma de {numA} / {numB} é: ", calculadora.div(5, 5))