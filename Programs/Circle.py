class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def getCircumference(self):
        return self.radius * 2 * 3.14


mycircle = Circle(5)

print(mycircle.getArea())
print(mycircle.getCircumference())
