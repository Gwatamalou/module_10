from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()

    def battle(self):
        count_day = 0
        while self.enemy > 0:
            sleep(1)
            count_day += 1
            self.enemy -= self.power
            if self.enemy < 0: self.enemy = 0
            print(f"{self.name} сражается {count_day} день(дня)..., осталось {self.enemy} воинов.")
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')
        return

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()