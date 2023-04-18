eng_words = ["computer", "scanner", "printer", "speakers", "keyboard", "mouse", "motherboard"]

rus_words = ["компьютер", "сканер", "принтер", "колонки", "клавиатура", "мышка", "материнская мышка"]

# index = eng_words.index("mouse")
# print(rus_words[index])

# {key : value } --> item

dictionary = {"computer": "компьютер", "scanner": "сканер", "printer": "принтер", "speakers": "колонки",
              "keyboard": "клавиатура", "mouse": "мышка", "motherboard": "материнская мышка"}

print(type(dictionary))
print(dictionary)
print(dictionary["mouse"])
