#lambda é eficiente para criação de funções simples
#exemplos:

dividir = lambda a, b: a / b

print(dividir(5,2))

incrementar_valores = lambda lista: [i+1 for i in lista]

print(incrementar_valores([1, 2, 3, 4]))

calculadora = {
    "soma": lambda a, b: a + b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b
}

soma = calculadora['soma']
print(f"A soma é {soma(2,5)}")
mul = calculadora["multiplicacao"]
print(f"A multiplicação é {mul(20,10)}")
div = calculadora["divisao"]
print(f"A divisao é {div(30,10)}")