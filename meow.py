import random

def cat_speak(text):
    words = text.split()
    cat_words = ["мяу", "мур", "пурр", "шшш", "фыр", "ня", "мяв"]
    translated = " ".join(random.choice(cat_words) for _ in words)
    return translated

user_text = input("Введите текст, который нужно перевести на кошачий: ")
print("Перевод на кошачий:", cat_speak(user_text))