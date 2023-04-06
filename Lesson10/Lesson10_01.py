# Roman Numerals (Римские цифры)
# В таблице приведены римские цифры для чисел от 1 до 10.
# 1 I 2 II
# 3 III
# 4 IV
# 5 	V
# 6 	VI
# 7 	VII
# 8 	VIII
# 9 	IX
# 10 	X

def convert(number):
    if number < 1 or number > 10:
        return "Error. Number should be between 1 and 10."

    if number == 1:
        answer = "I"
    elif number == 2:
        answer = "II"
    elif number == 3:
        answer = "III"
    elif number == 4:
        answer = "IV"
    elif number == 5:
        answer = "V"
    elif number == 6:
        answer = "VI"
    elif number == 7:
        answer = "VII"
    elif number == 8:
        answer = "VIII"
    elif number == 9:
        answer = "IX"
    else:
        answer = "X"

    return answer


def main():
    number = int(input("Input your number: "))
    print(convert(number))


def testing():
    result = " 1 --> I: " + str(convert(1) == "I")
    result += "\n2 --> II: " + str(convert(2) == "II")
    result += "\n3 --> III: " + str(convert(3) == "III")
    result += "\n4 --> IV: " + str(convert(4) == "IV")
    result += "\n5 --> V: " + str(convert(5) == "V")
    result += "\n6 --> VI: " + str(convert(6) == "VI")
    result += "\n7 --> VII: " + str(convert(7) == "VII")
    result += "\n8 --> VIII: " + str(convert(8) == "VIII")
    result += "\n9 --> IX: " + str(convert(9) == "IX")
    result += "\n10 --> X: " + str(convert(10) == "X")

    result += "\n0 --> Error: " + str(convert(0) == "Number should be between 1 and 10.")
    result += "\n100 --> Error: " + str(convert(100) == "Number should be between 1 and 10.")

    print(result)


testing()
