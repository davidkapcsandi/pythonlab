class Rectangle:
    def __init__(self, lenght , width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght * self.width

    def perimiter(self):
        return 2 * (self.lenght * self.width)
rect = Rectangle(5 , 10)
print(rect.area())
print(rect.perimiter())