def calc_factorial(number):
    if number < 0:
        return "Error. User data is invalid."

    factorial = 1
    n = 2

    while n <= number:
        factorial *= n
        n += 1

    return factorial


def main():
    number = int(input("Input your number: "))
    factorial = calc_factorial(number)
    msg = f"{number}! = {factorial}"
    print(msg)


def testing():
    msg = "calc_factorial(0) == 1 - " + str(calc_factorial(0) == 1)
    msg += "\ncalc_factorial(1) == 1 - " + str(calc_factorial(0) == 1)
    msg += "\ncalc_factorial(2) == 2 - " + str(calc_factorial(2) == 2)
    msg += "\ncalc_factorial(5) == 120 - " + str(calc_factorial(5) == 120)
    msg += "\ncalc_factorial(7) == 5040 - " + str(calc_factorial(7) == 5040)
    msg += "\ncalc_factorial(-1) == Error - " + str(calc_factorial(-1) == -1)
    msg += "\ncalc_factorial(-10) == Error - " + str(calc_factorial(-10) == -10)
    print(msg)


testing()

# if __name__ == "__main__":
# main()
