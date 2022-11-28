#WAP to differate between normal bike and super-bike ?

class Bike:
    def __init__(self, name, company, cc, topspeed, colour, superbike, year):

        self.name = name
        self.company = company
        self.cc = cc
        self.topspeed = topspeed
        self.colour = colour
        self.superbike = superbike
        self.year = year

    def is_superbike(self):
        
        if self.superbike == True:
            print("Yes its a superbike")

        else:
            print("No it is not a superbike")

    def details(self):

        print(f'name: {self.name}')
        print(f'company: {self.company}')
        print(f'cc: {self.cc}')
        print(f'topspeed: {self.topspeed}')
        print(f'colour: {self.colour}')
        print(f'superbike: {self.superbike}')
        print(f'manufactured year: {self.year}')


if __name__ == "__main__":

    b1 = Bike("Hayabusa", "Suzuki", 1000, 250, "Blue", True, 2004)
    print(b1.name)
    b1.details()
    b1.is_superbike()
    print('*'*50)

    b2 = Bike("Splender Plus", "Hero Honda", 100, 80, "Silver", False, 2008)
    b2.details()
    b2.is_superbike()

    print(b1.__dict__)
    print(b2.__dict__)

