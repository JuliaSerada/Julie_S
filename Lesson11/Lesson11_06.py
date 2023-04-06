from random import randrange

mood_number = 5

bad_mood = ":("
happy_mood = ":)"
shouted_mood = ":()"
nervous_mood = ":/"
neutral_mood = ":>"


def detect_mood():

    mood = randrange(mood_number)

    if mood == 1:
        msg = happy_mood
    elif mood == 2:
        msg = bad_mood
    elif mood == 3:
        msg = shouted_mood
    elif mood == 4:
        msg = nervous_mood
    elif mood == 5:
        msg = neutral_mood
    else:
        msg = Error

    return msg


def main():
    msg = detect_mood()
    print(msg)


main()
