from turtle import color
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):

        self.__color = color  # список цветов в формате RGB
        self.__sides = sides  # Список сторон целые числа
        self.filled = False        #закрашенный, bool
        self.__sides = []
        self.set_sides(*sides)
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):

        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:  # Цвет корректный
            return r, g, b
        else:
            return self.__color  # Цвет некорректный

    def set_color(self, r, g, b):
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color
    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]
        elif len(sides) == 1 and self.sides_count == 12 and sides[0] > 0:
            self.__sides = []
            for i in range(12):
                self.__sides.append(*sides)
        elif self.__sides != []:
            pass
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1  #Список сторон целые числа


    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._Figure__sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))) / self._Figure__sides[0]
        #print(self.__height, "высота")

    def get_square(self):
        St = (self.__height * self.sides[0]) / 2
        return St

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())