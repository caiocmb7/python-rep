""" tratar as exceções sempre do filho para o pai (do menos amplo para o mais amplo) """

lista = [1, 2, 3]

try: #Jeito normal de tratar a exceção
    acesso = lista[3]
except IndexError:
    print("Erro de acesso! Fora do range da lista requerida")

try:
    acesso = lista[3]
except: 
    print("Erro ao reproduzir a linha") #Exceção padrão

try:
    acesso = lista[3]
except BaseException as BE: #Exceção pai (muito ampla)
    print(f"Erro! {BE}")

try:
    abrir = open("lista.txt", "r") #note aqui que na reprodução ele vai mostrar apenas o primeiro erro, que é esse, os outros dois erros das linhas abaixo, são ignoradas
    acesso = lista[3]
    divisao = 10/0
except IndexError:
    print("Erro de acesso! Fora do range da lista requerida")
except ZeroDivisionError as Zero:
    print(f"Nao se pode dividir por zero! {Zero}")
except FileNotFoundError:
    print(f"Erro ao procurar o arquivo!")
except ModuleNotFoundError as ModuleNotFound:
    print(f"Erro na importação! {ModuleNotFound}")
else:
    print("Nao foi encontrado nenhum erro, script rodou com sucesso!")
finally:
    print("Recurso para sempre executar algo mesmo com a exceção")
    a = 10
    print(f"Foi criada a variável a com valor igual a {a}")

