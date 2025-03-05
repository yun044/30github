import random


def cat_speak(text):
    words = text.split()
    cat_words = ["мяу", "мур", "пурр", "шшш", "фыр", "ня", "мяв"]

    translated = []
    for word in words:
        if random.random() < 0.3:  # С шансом 30% оставляем слово как есть
            translated.append(word)
        else:
            translated.append(random.choice(cat_words))

        if random.random() < 0.2:  # Иногда добавляем дополнительное "кошачье" слово
            translated.append(random.choice(cat_words))

    return " ".join(translated)


user_text = input("Введите текст, который нужно перевести на кошачий: ")
print("Перевод на кошачий:", cat_speak(user_text))