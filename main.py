print("Программа для шифрования методом Цезаря")
while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    word = input("Enter e clear massage(Введите слово на английском): ")
    key = int(input("Please enter key (number from 1-25)(Введите ключ шифрования диапазоном 1-25): "))
    word = word.lower()
    wordX = ""
    for i in word:
        position = alphabet.find(i)
        newPosition = position + key
        if i in alphabet:
            wordX = wordX + alphabet[newPosition]
        else:
            wordX = wordX + i
    print("Your cipher is(Ваш шифр):", wordX)
