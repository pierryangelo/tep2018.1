class Car:
    def __init__(self, color, model, number_of_wheels):
        self.color = color
        self.model = model
        self.number_of_wheels = number_of_wheels

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.number_of_wheels = number