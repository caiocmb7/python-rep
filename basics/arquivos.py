#apenas escrever em um arquivo

def escrever_arquivo(texto):
    arquivo = open(r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_teste.txt", "w")
    arquivo.write(texto)
    arquivo.close()

escrever_arquivo("testando metodo escrever_arquivo")

#fazendo novamente essa parte, para perceber que o arquivo "arquivo_teste.txt" se torna branco novamente e só escreve o que está sendo passado

escrever_arquivo("testando metodo escrever_arquivo parte 2")

def limpar_arquivo():
    arquivo = open(r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_teste.txt", "w")
    arquivo.truncate()

def atualizar_arquivo(texto):
    arquivo = open(r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_teste.txt", "a") #percebe-se a diferença aqui
    arquivo.write(texto)
    arquivo.close()

limpar_arquivo()

atualizar_arquivo("\nteste 1")
atualizar_arquivo("\nteste 2")
atualizar_arquivo("\nteste 3")

limpar_arquivo() #apos essa linha, o arquivo .txt estará limpo (em branco)

escrever_arquivo("testando metodo ler_arquivo")

def ler_arquivo():
    arquivo = open(r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_teste.txt", "r")
    texto = arquivo.read()
    print(texto)

ler_arquivo()

def copiar_arquivo():
    import shutil
    shutil.copy(r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_teste.txt", r"C:\Users\Caio\Desktop\python codes\git\python-rep\basics\arquivo_copia.txt")

copiar_arquivo()





