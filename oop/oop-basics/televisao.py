class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def ligar(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False
    
    def globo(self):
        if self.canal != 10:
            self.canal = 10
        else:
            print("O canal atual já está na globo")

tv = Televisao()

print(f"\nA TV está: {tv.ligada}")
tv.ligar()
print(f"\nA TV está: {tv.ligada}")
print("\nO canal atual é:", tv.canal)
tv.globo()
print("\n ----- mudando de canal \n ----")
print("\nO canal atual é:", tv.canal)
print("\n ----- mudando de canal \n ----")
tv.globo()
