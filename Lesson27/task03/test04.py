class Super:
    def walk(self):
        print("I can walk. ")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is Subclass Super? - {issubclass(Subclass, Super)}")  # true
print(f"Is Super Subclass? - {issubclass(Super, Subclass)}")  # false
print(f"Is Super object? - {issubclass(Super, object)}")  # true
print(f"Is Subclass object? - {issubclass(Subclass, object)}")  # true
