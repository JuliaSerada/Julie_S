a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
d = int(input("Input d: "))

# max min arithmetic_avg geometrical_avg

if a > b and a > c and a > d:
    max_value = a
else:
    max_value = b
if b > a and b > c and b > d:
    max_value = b
else:
    max_value = c
if c > a and c > b and c > d:
    max_value = c
else:
    max_value = d

msg = f"Max value is {max_value}"
print(msg)
