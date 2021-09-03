class Calculadora:
    def __init__(self, numA, numB):
        self.valor_A = numA
        self.valor_B = numB

    def soma(self):
        return self.valor_A + self.valor_B
    
    def div(self):
        return self.valor_A / self.valor_B

    def mul(self):
        return self.valor_A * self.valor_B

#instanciar o objeto
calculadora = Calculadora(2,3)

#nesse caso dá pra instanciar os valores para dizer quais são no print, dif. da v1
print(f"\nA soma de {calculadora.valor_A} + {calculadora.valor_B} é:", calculadora.soma())

print(f"\nA multiplicação de {calculadora.valor_A} * {calculadora.valor_B} é:", calculadora.mul())

print(f"\nA divisão de {calculadora.valor_A} / {calculadora.valor_B} é:", round(calculadora.div(), 2))