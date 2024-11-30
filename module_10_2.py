from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!'+'\n')
        enemy = 100
        for j in range(100):
            enemy -= self.power
            print(f'{self.name}: сражается {j+1} день(дня)..., осталось {enemy} воинов.'+'\n')
            if enemy == 0:
                print(f'{self.name} одержал победу спустя {j+1} дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')