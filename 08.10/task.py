class Vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Стоимость: {self.price} руб.")
        print("-" * 30)


class Car(Vehicle):
    def __init__(self, brand, model, year, price, horsepower):
        super().__init__(brand, model, year, price)
        self.horsepower = horsepower

    def display_info(self):
        super().display_info()
        print(f"Лошадинных сил: {self.horsepower}")
        print("-" * 30)


class Truck(Vehicle):
    def __init__(self, brand, model, year, price, load_capacity):
        super().__init__(brand, model, year, price)
        self.load_capacity = load_capacity

    def display_info(self):
        super().display_info()
        print(f"Грузоподъёмность: {self.load_capacity} кг")
        print("-" * 30)


car = Car("Toyota", "Camry", 2022, 3000000, 350)
truck = Truck("Volvo", "FH16", 2021, 8500000, 25000)

car.display_info()
truck.display_info()
