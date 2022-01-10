word = input("Введите слово: ")
word = word.lower()
if word[0] != "а" and "е" and "и" and "о" and "у":
    nw = word[1:] + word[0] + "ау"
else:
    nw = word + "вау"
print(nw.lower())
