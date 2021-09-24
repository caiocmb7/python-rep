class Shape():
    name = "shape 2"
    def __init__(self):
        self.color = "red"
    
    def perimeter(self):
        return self.height*2 + self.width*2
    
    def area(self):
        raise NotImplementedError()

class Square(Shape):
    def __init__(self, side):
        self.side = side
        super().__init__()

    def perimeter(self):
        return f"O perímetro de lado {self.side} é {self.side * 4}"

    def area(self):
        return f"A área de lado {self.side} é {self.side ** 2}"

class Rectangle(Shape):
    name = "rectangle"

    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def perimeter(self):
        return f"O perímetro do retângulo cujo valores dos lados são '{self.width}' e '{self.height}' é {self.height*2 + self.width*2}"

if __name__ == "__main__":
    shape = Shape()
    rectangle = Rectangle(1, 2)
    print(rectangle.perimeter())
    print(rectangle.name)
    square = Square(1)
    print(square.name)
    print(square.perimeter())
    print(square.area())

