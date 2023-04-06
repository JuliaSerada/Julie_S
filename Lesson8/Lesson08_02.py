# birth - 3 heads
# 0 .. 100   -+3 heads
# 101 .. 200 -+2 heads
# 201 .. -+1 head
age = int(input("Input dragon age: "))
total = 3
if age <= 100:
    total += age * 3
elif age <= 200:
    total += 300 + (age - 100) * 2
else:
    total += 300 + 200 + (age - 200) * 1
msg = f"Dragon has {total} heads"
print(msg)
