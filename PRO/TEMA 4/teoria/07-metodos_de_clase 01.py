class Foo:
    x = 10

    def __init__(self, x) -> None:
        self.x = x

    @classmethod
    def get_x_class(cls):
        return cls.x

if __name__ == '__main__':

    f = Foo(-2)
    print(f.x)
    print(Foo.x)
    f.x = 20
    Foo.x = 30
    print(f.x)
    print(Foo.x)
    print ("****")
    print("---", Foo.get_x_class())
    print( f.get_x_class() )
