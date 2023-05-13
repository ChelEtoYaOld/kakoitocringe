
class Human:
    def __init__(self, name='Human'):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *mikrochely):
        self.passengers += mikrochely

    def print_passengers(self):
        if self.passengers:
            print(f'Names of passengers in {self.brand}:')
            for p in self.passengers:
                print(p.name)
            else:
                print(f'There are no passengers in {self.brand}:')

vasya = Human('Vasya')
tamara = Human('Tamara')
andrei = Human('Andrei')
car = Auto('Bugatti')
car.add_passengers(vasya, tamara, andrei)
car.print_passengers()

