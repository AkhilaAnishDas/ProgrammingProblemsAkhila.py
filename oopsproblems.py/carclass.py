class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(self.brand, self.model, "is driving...")


# Example
c = Car("Honda", "City")
c.drive()
