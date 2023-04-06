# Сообщение от учителя
# до 13 включительно – детство (childhood);
# от 14 до 34 – молодость (youth);
# от 35 до 59 – зрелость (maturity);
# от 60 – 150 старость (old age).

age = int(input("Input your age: "))

if 0 <= age <= 13:
    answer = "childhood"
elif 14 <= age <= 34:
    answer = "youth"
elif 35 <= age <= 59:
    answer = "maturity"
elif 60 <= age <= 150:
    answer = "old age"
else:
    answer = "Data is false"
msg = f"Your age is {answer}"

print(msg)
