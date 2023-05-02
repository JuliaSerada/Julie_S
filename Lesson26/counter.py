class Counter:
    def __init__(self, count=0):
        if count >= 0:
            self.__count = count
        else:
            self.__count = 0

    @property
    def count(self):  # реализация метода инкапсуляции через get_count + 2 нижних подчеркивания __count
        return self.__count

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count != 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def __str__(self):
        return "Counter: " + str(self.__count)
