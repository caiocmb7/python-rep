while True:
    max = int(input())
    for i in range(max):
        a, b = [int(x) for x in input().split()]
        if (a < b):
            print("<")
        elif (a > b):
            print(">")
        elif (a == b):
            print("=")