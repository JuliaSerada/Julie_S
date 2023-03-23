# 12345 -> 54321

#n = input(12345)[::-1]
#print(n)

number = int (input ("Input your number: "))
number_copy = number
reverse_number = number % 10
number //=10
reverse_number *=10