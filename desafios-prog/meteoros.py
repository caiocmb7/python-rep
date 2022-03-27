cont_test = 0

while True:
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if(x1 == y1 and y1 == x2 and x2 == y2 and x1 == 0):
        break
    else:
        num_meteoros = int(input())
        cont_test = cont_test + 1
        cont = 0
        for i in range(num_meteoros):
            ponto_x, ponto_y = [int(x) for x in input().split()]
            if (ponto_x >= x1 and ponto_x <= x2) and (ponto_y <= y1 and ponto_y >= y2):
                cont = cont + 1
        print (f"Teste {cont_test}")
        print(f"{cont}")