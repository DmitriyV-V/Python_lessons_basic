import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.lenA = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.lenB = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self.lenC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    def spuare_triangle(self):  # Площадь треугольника
        self.spuare = math.sqrt(self.perimeter() * (self.perimeter() - self.lenA) * (self.perimeter() - self.lenB) *
                                (self.perimeter() - self.lenC))
        return round(self.spuare, 2)

    def height_triangle(self):  # Высота треугольника
        return round(2 / self.lenA * self.spuare_triangle(), 2)

    def perimeter(self):  # Периметр треугольника
        return round(self.lenA + self.lenB + self.lenC, 2)


triangle = Triangle(5, 7, 1, 4, 8, 13)

square_triangle = triangle.spuare_triangle()
height_triangle = triangle.height_triangle()
perimeter_triangle = triangle.perimeter()

print(f"Square triangle - {square_triangle}")
print(f"Height triangle - {height_triangle}")
print(f"Perimeter triangle - {perimeter_triangle}")
print()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.lenA = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.lenB = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self.lenC = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        self.lenD = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)

    def perimeter(self):
        return round(self.lenA + self.lenB + self.lenC + self.lenD, 2)

    def length_trapezium(self):
        return self.lenA, self.lenB, self.lenD, self.lenD

    def is_trapezium(self):
        if self.lenA == self.lenC and \
              (self.x4 - self.x1) / self.lenD == (self.x3 - self.x2) / self.lenB or \
              self.lenB == self.lenD and \
              (self.x4 - self.x3) / self.lenC == (self.x2 - self.x1) / self.lenA:
            return True
        else:
            return False

    def square_trapezium(self):
        square = abs(((self.x1 - self.x3) * (self.y2 - self.y3) -
                      ((self.x2 - self.x3) * (self.y1 - self.y3))) / 2) + \
                abs(((self.x1 - self.x3) * (self.y4 - self.y3) -
                     ((self.x4 - self.x3) * (self.y1 - self.y3))) / 2)
        return square


trapezium = Trapezium(1, 1, 11, 1, 3, 5, 9, 5)

is_trapezium = trapezium.is_trapezium()
perimeter_trap = trapezium.perimeter()
square_trap = trapezium.square_trapezium()


print(f"Является ли фигура трапецией - {is_trapezium}")
print(f"Perimeter trapezium - {perimeter_trap}")
print(f"Square trapezium - {square_trap}")
