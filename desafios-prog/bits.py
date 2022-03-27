notas = [50, 10, 5, 1]
res = [0, 0, 0, 0]
valores = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    valores = valores + 1
    for i in range(4):
        res[i] = int(valor / notas[i])
        valor = valor % notas[i]

    print (f"Teste {valores}")
    print (res[0], res[1], res[2], res[3], "\n")



"""
cont = 0

def cedulas(valor):
    novo = valor
    if valor // 50 >= 1:
        I = valor // 50
        novo = valor - ((valor // 50) * 50)
    elif novo // 10 >= 1:
        J = novo // 10
        novo = novo - (10 * novo // 10)
    elif novo // 5 >= 1:
        K = novo // 5
        novo = novo - (5 * novo // 5)
    elif novo >= 1:
        L = (50 * I) + (J * 10) + (K * 5)
    else:
        I, J, K, L = 0
    cont = cont + 1
    print(f"Teste {cont}")
    print(f"{I} {J} {K} {L} \n")

if  __name__ == "__main__":
    valor = input("")
    cedulas(valor)
    print(f"Teste {cont}")
    
    print("\n")
"""