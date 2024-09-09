cards = []
classes = ["S","C","H","D"]
for clas in classes:
    for number in range(10):
        cards.append(clas + str(number))
    cards.append(clas + "J")
    cards.append(clas + "Q")
    cards.append(clas + "K")
