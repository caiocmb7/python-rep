def splitar(lista):
    return ([i for item in lista for i in item.split("-")])

lista =  ['85-954594', '56-43434', '85-954593', '56-5656578', '43-540576']
lista_splitada = splitar(lista)
print(lista_splitada)

lista_numeros = []
for i in range(len(lista_splitada)):
    if(i % 2 == 0):
        lista_numeros.append(lista_splitada[i])

print(lista_numeros)

lista_limpa = set(lista_numeros)
print(lista_limpa)

tamanho = len(lista_limpa)
print(tamanho)