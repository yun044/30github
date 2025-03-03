import random

choices = {
    "камень": {"ножницы", "ящерица"},
    "ножницы": {"бумага", "ящерица"},
    "бумага": {"камень", "спок"},
    "ящерица": {"спок", "бумага"},
    "спок": {"камень", "ножницы"}
}

def get_computer_choice():
    return random.choice(list(choices.keys()))

# Функция определения победителя
def determine_winner(player, computer):
    if player == computer:
        return "Ничья!"
    elif computer in choices[player]:
        return "Ты победил! 🎉"
    else:
        return "Компьютер выиграл! 🤖"

# Функция для нормализации ввода (убирает пробелы, приводит к нижнему регистру)
def normalize_choice(choice):
    return choice.strip().lower()


def play_game(rounds=3):
    player_score, computer_score, draws = 0, 0, 0

    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага' (и не только)! 🤖")
    print(f"Вы играете до {rounds} побед!")

    while player_score < rounds and computer_score < rounds:
        player_input = input("Выбери: Камень, Ножницы, Бумага, Ящерица или Спок? ").lower()
        player_choice = normalize_choice(player_input)

        if player_choice not in choices:
            print("Ошибка: некорректный ввод! Попробуй снова.")
            continue

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice.capitalize()}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "Ты победил" in result:
            player_score += 1
        elif "Компьютер выиграл" in result:
            computer_score += 1
        else:
            draws += 1

        print(f"Счет: Ты {player_score} - {computer_score} Компьютер (Ничьи: {draws})\n")

    if player_score > computer_score:
        print("🎉 Поздравляю, ты выиграл серию!")
    else:
        print("🤖 Компьютер победил в серии!")

if __name__ == "__main__":
    play_game(rounds=3)