import os
import shutil

input_recebido = r"C:\Users\Caio\Desktop\python codes\git\python-rep\projetos\3. jpg_to_png\imagem_test"
os.chdir(input_recebido)
imagens_destino = input_recebido + "\\imagens_transformadas"

try:
    os.makedirs(input_recebido + "\\imagens_transformadas")
except FileExistsError as Err:
    print(f"A Pasta {imagens_destino} já existe.")


files = os.listdir(input_recebido)

for f in files:
    if (f.endswith(".png")):
        shutil.move(f, input_recebido + "\\imagens_transformadas")
print('Imagens transformadas e transferidas para a pasta "imagens_transformadas"')
