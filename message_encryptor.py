import random
import string

def generate_cipher():
    letters = string.ascii_letters + string.digits + " .,!?@#$%^&*"
    shuffled = list(letters)
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled)), dict(zip(shuffled, letters))

# Шифровка. Работаем с латиницей!

def encrypt(text, cipher):
    return "".join(cipher.get(char, char) for char in text)

# Расшифровываем
def decrypt(text, decipher):
    return "".join(decipher.get(char, char) for char in text)

cipher, decipher = generate_cipher()

while True:
    print("\n Меню:")
    print("1 - Зашифровать сообщение")
    print("2 - Расшифровать сообщение")
    print("3 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        message = input("Введите сообщение: ")
        encrypted = encrypt(message, cipher)
        print(f" Зашифровано: {encrypted}")
    elif choice == "2":
        message = input("Введите зашифрованное сообщение: ")
        decrypted = decrypt(message, decipher)
        print(f" Расшифровано: {decrypted}")
    elif choice == "3":
        print("👋 Выход...")
        break
    else:
        print("⚠ Ошибка: выберите правильный пункт меню!")