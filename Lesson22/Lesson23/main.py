from student import Student


def main():
    st1 = Student("Alex", 20, 10)
    st2 = Student("Kate", 18, 7)
    st3 = Student("Peter", 21, 9)
    st4 = Student()

    # st1.init("Alex", 20, 10)
    # st2.init("Kate", 18, 9)

    # print(st1.name)
    # print(getattr(st1, "name"))
    # print(st1.__getattribute__("name"))

    # del st1.name
    # delattr(st1, "mark")
    # st1.__delattr__("age")

    # st1.name = "Alex"
    # setattr(st1, "name", "Peter")
    # st1.__setattr__("name", "Olya")

    # print(vars(st1))


# print(st1.__dict__)
# print(help(st1))
# print(dir(st1))


if __name__ == "__main__":
    main()
