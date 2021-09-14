import time

def contador_tempo(t):
    while t:
        minutos, segundos = divmod(t, 60) #receber o tempo e dividir em 60 para identificar min, seg
        timer = "{:02d}:{:02d}".format(minutos, segundos)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("\n Time completed!!")

if __name__ == "__main__":
    t = input("Digite um valor: ")
    contador_tempo(int(t))