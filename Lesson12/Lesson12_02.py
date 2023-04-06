# heads or tails

from random import randrange

side_count = 2


def throw_coin(count):
    if count <= 0:
        return 0, 0

    heads = 0
    counter = 0

    while counter < count:
        side = randrange(side_count)

        if side == 0:
            heads += 1

        counter += 1

    return heads, count - heads


def main():
    count = int(input("Input count of throwing: "))
    heads, tails = throw_coin(count)

    msg = f"Count of heads is {heads}, count of tails is {tails}"
    print(msg)


main()
