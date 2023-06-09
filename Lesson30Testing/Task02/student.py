from human import Human


class Student(Human):
    def hello(self):
        super().hello()
        print(" I'm a student.")


def main():
    h = Human("Trueman")
    st = Student("Alex")
    h.hello()
    st.hello()


if __name__ == "__main__":
    main()
