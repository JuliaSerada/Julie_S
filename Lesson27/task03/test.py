class Super1:
    def walk(self):
        print("I can walk. ")


class Super2:
    def walk(self):
        print("I can walk. ")


class Subclass(Super):
    pass


sub = Subclass()
sub.walk()
