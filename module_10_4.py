from threading import Thread
from random import randint
from time import sleep
from queue import Queue


# Класс Table:
# Объекты этого класса должны создаваться следующим способом - Table(1)
class Table:
    def __init__(self, number):
        # Обладать атрибутами number - номер стола и guest - гость,
        # который сидит за этим столом (по умолчанию None)
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        # Обладать атрибутом name - имя гостя.
        super().__init__()
        self.name = name

    # Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
    def run(self):
        sleep(randint(3, 10))


class Cafe:
    # Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    def __init__(self, *tables):
        # Обладать атрибутами queue - очередь (объект класса Queue)
        self.queue = Queue()
        # и tables - столы в этом кафе (любая коллекция).
        self.tables = list(tables)

    # Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    def guest_arrival(self, *guests):
        # Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        for guest in guests:
            # Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
            for table in self.tables:
                # Для проверки значения на None используйте оператор is (table.guest is None).
                if table.guest is None:
                    table.guest = guest
                    # запускать поток гостя и выводить на экран строку
                    guest.start()
                    # "<имя гостя> сел(-а) за стол номер <номер стола>".
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break

    # Метод discuss_guests(self):
    # Этот метод имитирует процесс обслуживания гостей.
    def discuss_guests(self):
        # Обслуживание должно происходить пока очередь не пустая (метод empty)
        # или хотя бы один стол занят.
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                # Если за столом есть гость(поток) и гость(поток) закончил приём пищи
                # (поток завершил работу - метод is_alive), то вывести строки
                if table.guest is not None and not table.guest.is_alive():
                    # "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)"
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    # и "Стол номер <номер стола> свободен".
                    print(f"Стол номер {table.number} свободен")
                    # Так же текущий стол освобождается (table.guest = None).
                    table.guest = None
                    # Если очередь ещё не пуста (метод empty) и
                    # стол один из столов освободился (None),
                    if not self.queue.empty():
                        # то текущему столу присваивается гость взятый из очереди (queue.get()).
                        # Для добавления в очередь используйте метод put, для взятия - get.
                        next_guest = self.queue.get()
                        table.guest = next_guest

                        # Далее запустить поток этого гостя (start)
                        next_guest.start()

                        # Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди
                        # и сел(-а) за стол номер <номер стола>"
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    sleep(1)
# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()


