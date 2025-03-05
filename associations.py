import random
import json
import os

# Файл для хранения ассоциаций
FILE_NAME = "associations.json"

# Базовые ассоциации
default_associations = {
    "кот": ["молоко", "мяу", "шерсть", "сон", "охота"],
    "солнце": ["жара", "день", "лето", "лучи", "энергия"],
    "книга": ["чтение", "знание", "история", "страницы", "автор"],
    "дорога": ["машина", "путешествие", "асфальт", "движение", "расстояние"],
    "музыка": ["мелодия", "песня", "звук", "ритм", "инструмент"]
}


def load_associations():
    """Загружает ассоциации из файла, если он существует, иначе возвращает стандартные."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return default_associations


def save_associations():
    """Сохраняет текущие ассоциации в файл."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(associations, file, ensure_ascii=False, indent=4)


def find_association(word):
    """Ищет случайную ассоциацию к введенному слову"""
    word = word.lower().strip()
    if word in associations:
        return random.choice(associations[word])
    return None


def add_association(word, new_association):
    """Добавляет новую ассоциацию к слову"""
    word = word.lower().strip()
    new_association = new_association.lower().strip()

    if word in associations:
        if new_association not in associations[word]:
            associations[word].append(new_association)
    else:
        associations[word] = [new_association]

    save_associations()  # Сохраняем изменения


# Загружаем данные
associations = load_associations()

print("Введите слово, и я найду к нему ассоциацию! (Напишите 'выход' для завершения)")
while True:
    user_input = input("\nВведите слово: ").strip().lower()

    if user_input == "выход":
        print("До встречи! 😊")
        break

    association = find_association(user_input)

    if association:
        print(f"Ассоциация: {association}")
    else:
        print("Я пока не знаю ассоциаций к этому слову...")
        new_association = input("Введите ассоциацию к этому слову: ").strip()
        if new_association:
            add_association(user_input, new_association)
            print(f"Добавлено! Теперь '{user_input}' ассоциируется с '{new_association}' 😊")