cont = 0

num_casos = int(input())
for i in range(num_casos):
    lista = []
    limite_inf = int(input())
    limite_sup = int(input())
    for k in range(limite_inf, limite_sup+1): 
        if(k % 2 == 1):
            lista.append(k)
        soma = sum(lista)
    cont = cont + 1
    print(f"Caso {cont}: {soma}")
        