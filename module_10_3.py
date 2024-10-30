import threading
import random
import time


# Необходимо создать класс Bank со следующими свойствами:

class Bank:
    def __init__(self):
        # balance - баланс банка (int)
        self.balance = 0

        # lock - объект класса Lock для блокировки потоков.
        self.lock = threading.Lock()

        # Метод deposit:

    def deposit(self):
        # Будет совершать 100 транзакций пополнения средств.
        for _ in range(100):
            # Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
            money = random.randint(50, 500)
            self.balance += money
            # Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(),
            # то разблокировать его методом release.
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            # После увеличения баланса должна выводится строка
            # "Пополнение: <случайное число>. Баланс: <текущий баланс>".
            print(f"Пополнение: {money}. Баланс: {self.balance}")
            # Также после всех операций поставьте ожидание в 0.001 секунды,
            # тем самым имитируя скорость выполнения пополнения.
            time.sleep(0.001)

    # Метод take:
    def take(self):

        # Будет совершать 100 транзакций снятия.
        for _ in range(100):

            # Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
            money = random.randint(50, 500)

            # В начале должно выводится сообщение "Запрос на <случайное число>".
            print(f"Запрос на {money}")
            # Далее производится проверка: если случайное число меньше
            # или равно текущему балансу, то произвести снятие
            if money <= self.balance:
                # уменьшив balance на соответствующее число
                self.balance -= money

                # И вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
                print(f"Снятие: {money}. Баланс: {self.balance}")

                # Если случайное число оказалось больше баланса, то вывести строку
                # "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquiere.
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
