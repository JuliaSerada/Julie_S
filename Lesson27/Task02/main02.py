from test06 import Doctor
from student import Student
from worker import Worker


def main():
    doc = Doctor("Watson", 55, True, 45)
    student = Student("Alex", 20, True, 10)
    worker = Worker("Volodya", 45, True, 2500)

    print(doc)
    print(student)
    print(worker)


if __name__ == "__main__":
    main()
