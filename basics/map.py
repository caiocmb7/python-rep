lista = [1, 2, 3, 4, 5, 6]

def acrescentar_lista(n):
    return n + 1

map_lista = map(acrescentar_lista, lista)

lista_acrescentada = list(map_lista)

print(lista_acrescentada)