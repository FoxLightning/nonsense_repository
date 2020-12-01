from collections import namedtuple

class GoAt:
    legs_number = [1,2,3,4]
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def __str__(self):
        s = "weight = {}, height = {}, legs = {}".format(self.weight, self.height, self.legs_number)
        return s
a = GoAt(90, 60)
b = GoAt(60, 50)
a.legs_number.append(5)
c = GoAt(70, 55)
print(a)
print(b)
print(c)

Point = namedtuple("Точка", "x y z")
A = Point(1,2,3)

print(A)

