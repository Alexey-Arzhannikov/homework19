from random import choice, randint
class Building:
    total = 0

    def __init__(self, name='Объект'):
        self.name = name
        self.numberOfFloors = randint(1, 100)
        self.buildingType = choice(['монолитный', 'кирпичный', 'панельный'])
        self.street = choice(['Победы', 'Терешковой', 'Неделина', 'Октябрьская', 'Катукова'])
        Building.total += 1

    def __str__(self):
        return str(f'\n {self.__dict__}')

build_list = []
for i in range(1, 41):
    build_list.append(Building('Объект №'+str(i)))

print(*build_list)
