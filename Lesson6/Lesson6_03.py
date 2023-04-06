a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
exist = a + b > c and a + c > b and c + b > a
result = exist and (a * a + b * b == c * c
                    or a * a + c * c == b * b
                    or b * b + c * c == a * a)

msg = "Is the triangle rectangular?"
msg += "\n" + ("Yes, the triangle rectangular is right angled."
        if result else "No, the triangle rectangular isn't right angled.")

print(msg)
