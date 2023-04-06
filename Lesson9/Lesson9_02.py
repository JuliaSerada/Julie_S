# football team girls 15-18
# age and m or f

age = int(input("Input your age: "))
gender = input("Input your gender (m/f): ")

if 15 <= age <= 18 and gender == "f":
    answer = "True"
else:
    answer = "False"
msg = "Yes" if answer else "No"
print(msg)
