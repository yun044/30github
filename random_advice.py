import random

# Список советов
advice_list = [
    "Всегда делай бэкапы важных файлов!",
    "Не бойся задавать вопросы.",
    "Учись на своих ошибках.",
    "Пей больше воды и отдыхай.",
    "Разбивай большие задачи на маленькие.",
    "Лучший способ учиться – практика!"
]

def get_random_advice():
    """Выводит случайный совет"""
    print("\n💡 Совет дня: " + random.choice(advice_list))

def add_advice():
    """Добавляет новый совет в список"""
    new_advice = input("\nВведите новый совет: ")
    advice_list.append(new_advice)
    print("✅ Совет добавлен!")

def show_all_advice():
    """Показывает все советы"""
    print("\n📜 Все советы:")
    for i, advice in enumerate(advice_list, start=1):
        print(f"{i}. {advice}")

def main():
    while True:
        print("\n📌 Меню:")
        print("1️⃣ Получить случайный совет")
        print("2️⃣ Добавить новый совет")
        print("3️⃣ Показать все советы")
        print("4️⃣ Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            get_random_advice()
        elif choice == "2":
            add_advice()
        elif choice == "3":
            show_all_advice()
        elif choice == "4":
            print("👋 До встречи!")
            break
        else:
            print("⚠ Ошибка: выберите правильный пункт меню!")

if __name__ == "__main__":
    main()