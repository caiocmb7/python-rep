#usa-se {} para declarar conjuntos - sets

set1 = {1,2,3,5,7,8,9,2,5,11,56,342,5312,53,232,53,1231,566546}

set2 = {23,1,5435,21,232,52,32,15,6,33,56,2243,453,2,13,56,7}

print("\nA união dos dois conjuntos é:", set1.union(set2))

print("\nA interseção dos dois conjuntos é:", set1.intersection(set2))

print("\nA diferença do conjunto 1 - conjunto 2 é:", set1.difference(set2))

print("\nA diferença do conjunto 2 - conjunto 1 é:", set2.difference(set1))

''' checar se um conjunto é subconjunto do outro '''

print("\nO conjunto 1 é subconjunto do conjunto 2:", set1.issubset(set2))

''' existe tbm a função superset, que é o contrário do subset '''

print("\nO conjunto 1 é superconjunto do conjunto 2:", set1.issuperset(set2))

''' a parte importante para aprender set é pelo seguinte fato a seguir: transformar uma lista em set para retirar os elementos repetidos'''

lista = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 55, 64, 34, 1313, 2, 3, 3232]

lista_para_conjunto = set(lista)

print(f"\nA lista: {lista} se transformou em conjunto: {lista_para_conjunto}")