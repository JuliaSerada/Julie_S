# check count even value

def count_even_value(ls):
    count = 0

    for item in ls:
        if item % 2 == 0:
            count += 1

    return count


def test():
    print(count_even_value([1, 2, 3, 4]) == 2)
    print(count_even_value([2, 4, 6, 8]) == 4)
    print(count_even_value([1, 3, 5, 7]) == 0)


if __name__ == "__main__":
    test()
