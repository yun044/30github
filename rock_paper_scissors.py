import random

def get_computer_choice():
    return random.choice(["Камень", "Ножницы", "Бумага"])

def determine_winner(player, computer):
    if player == computer:
        return "Ничья!"
    elif (player == "Камень" and computer == "Ножницы") or \
         (player == "Ножницы" and computer == "Бумага") or \
         (player == "Бумага" and computer == "Камень"):
        return "Ты победил! 🎉"
    else:
        return "Компьютер выиграл! 🤖"

if __name__ == "__main__":
    player_choice = input("Выбери: Камень, Ножницы или Бумага? ").capitalize()
    if player_choice not in ["Камень", "Ножницы", "Бумага"]:
        print("Ошибка: некорректный ввод!")
    else:
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))