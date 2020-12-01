class Auto:
    def __init__(self):
        self.x = "Auto init"
    def ride(self):
        print("Riding on a ground")
    def swim(self):
        print("no swim")


class Boat:
    def __init__(self):
        self.x = "Boat init"
    def swim(self):
        print("Sailing in the ocean")


class Amphibian(Auto, Boat):
    def __init__(self):
        super().__init__(Boat)



a = Amphibian()

print(a.x)
a.ride()
a.swim()

