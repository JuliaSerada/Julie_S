import Lesson21_view
import Lesson21_Logic
import util


# controller
def main():
    while True:
        size = int(input("Input size of list: "))
        if size > 0:
            break
        else:
            Lesson21_view.write("Error. User data is invalid.")

    ls = util.create_list(size)

    util.rnd_init_list(ls, -50, 50)
   # util.user_init_list(ls)

    second = Lesson21_Logic.find_second_max_value(ls)

    msg = f"Second max value is {second}."

    Lesson21_view.write(ls)
    Lesson21_view.write(msg)


if __name__ == "__main__":
    main()
