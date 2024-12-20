import math

class Figure:
    sides_count = 0
    
    def __init__(self, color, *sides):
        self.__sides = list(sides)                                      # стороны
        self.__color = list(color)
        self.filled = False                                             # заполненный

        if len(self.__sides) != self.sides_count:
                self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color
    
    def __is_valid_color(self, r, g, b):                                      # допустимый цвет
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))
    
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):                                                 # получить
        return self.__sides

    def __len__(self):
        return sum(self.__sides)
    
    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)


    def set_sides(self, *new_sides):                                     # установить
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            
class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.update_radius()

            
    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.update_radius()

    def update_radius(self):
        sides = self.get_sides()
        if sides[0] > 0:
            self.__radius = sides[0] / (2 * math.pi)
        else:
            self.__radius = 0

    def get_radius(self):
        return self.__radius

class Triangle(Figure):
    sides_count = 3

    def get_square(self):                                            # площадь
        a, b, c = self.get_sides()
        if a + b > c and a + c > b and b + c > a:
            p = sum(self.get_sides()) / 2
            return int(math.sqrt(p * (p - a) * (p - b) * (p - c)))
        return 0

class Cube(Figure):
    sides_count = 12
    
    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        elif len(sides) != self.sides_count:
            sides = [1] * self.sides_count

        super().__init__(color, *sides)

    def get_volume(self):                                            # объем
        return self.get_sides()[0] ** 3

triangle1 = Triangle((200, 200, 100), 3, 4, 5)
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

triangle1.set_color(180, 260, 60)
print(triangle1.get_color())

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())

print(triangle1.get_square())

triangle1.set_sides(10, 6)
print(triangle1.get_sides())


        
   
        
       
        