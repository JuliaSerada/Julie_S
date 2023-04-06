
a = int(input("Input a: "))
b = int(input("Input b: "))


max = a if a > b else b
min = a if a < b else b

msg = "Max value is " + str(max)
msg += "\nMin value is " + str(min)

print(msg)