print()     # Отступ


# Создайте:
# 2 класса родителя: Animal, Plant

# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    # Метод eat должен работать следующим образом:
    def eat(self, food):

        # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
        # меняется атрибут fed на True.
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True

        # Если переданное растение (food) не съедобное - выводит на экран "<self.name>
        # не стал есть <food.name>", меняется атрибут alive на False.
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
    # Т.е если животному дать съедобное растение, то животное насытится,
    # если не съедобное - погибнет.


# Для класса Plant атрибут edible = False(съедобность),
# name - индивидуальное название каждого растения
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    # Заглушка
    pass


class Fruit(Plant):
    # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
    def __init__(self, name):
        self.edible = True
        self.name = name


# Создайте объекты классов и проделайте действия затронутые в примере
# результата работы программы.

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

















