from PIL import Image 
import os


def png_to_jpg():
    input_path = str(input("Qual o caminho da pasta: "))
    for filename in os.listdir(input_path):
        current_img = Image.open(input_path + '\\' + filename)
        current_img.save(input_path + '\\' +
                        filename + '.png', 'PNG')

    print("Finalizado!")

if __name__ == "__main__":
    png_to_jpg()
