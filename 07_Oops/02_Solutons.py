class Car:
    def __init__(self, brand, model):
        self.brand =brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_Car = Car("Toyota","Corolla")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())

my_new_car=Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())