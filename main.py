print("Программа для шифрования и расшифровки методом Цезаря")
while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    x = int(input("Encrypt/Decrypt(Зашифровать/Разшифровать)1/2: "))
    if x == 1:
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
    elif x == 2:
        word = input("Enter e cipher massage(Введите шифр на английском): ")
        key = int(input("Please enter key (number from 1-25)(Введите ключ шифрования диапазоном 1-25): "))
        word = word.lower()
        wordX = ""
        for i in word:
            position = alphabet.find(i)
            newPosition = position - key
            if i in alphabet:
                wordX = wordX + alphabet[newPosition]
            else:
                wordX = wordX + i
        print("Your word is(Ваше слово):", wordX)
    else:
        print("You entered the wrong command, try again(Вы ввели не верную комнанду, попробуйте еще раз)")
