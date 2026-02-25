from abc import ABC, abstractmethod

class Polygon (ABC) :

    @abstractmethod
    def noofsides (self):
        pass

class Triangle(Polygon):

    # overriding abstract method
    def noofsides (self):
        print("I have 3 sides")

class Pentagon (Polygon):

    # overriding abstract method
    def noofsides (self):
        print("I have 5 sides")

class Hexagon (Polygon) :

# overriding abstract method
    def noofsides (self):
        print("I have 6 sides")

class Quadrilateral(Polygon) :

# overriding abstract method
    def noofsides (self):
        print("I have 4 sides")


if __name__ == '__main__':
# principal

    R = Triangle()
    R. noofsides ()

    K = Quadrilateral()
    K. noofsides ()

    R = Pentagon ( )
    R. noofsides ()

    K = Hexagon ( )
    K. noofsides ()

    print ("-----")

    # no se puede instanciar objetos de las clases abstractas

    # P = Polygon ()