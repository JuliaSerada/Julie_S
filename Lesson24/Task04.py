dictionary = {"Alex": 10, "Peter": 9, "Victor": 7, "Anna": 8, "Kate": 8, "Vova": 10, "Nikita": 8}

# print(dictionary["Alice"])
print(dictionary.get("Alice", 0))  # none (error)
print(dictionary.get("Anna"))


