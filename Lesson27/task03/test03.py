class Super:
    def walk(self):
        print("I can walk. ")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is base Super? - {isinstance(base, Super)}")      #true
print(f"Is base Subclass? - {isinstance(base, Subclass)}")   #false
print(f"Is sub Super? - {isinstance(sub, Super)}")             #true
print(f"Is sub Subclass? - {isinstance(sub, Subclass)}")     #true