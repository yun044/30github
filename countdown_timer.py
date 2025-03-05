import time
import sys

def count_down(seconds):
    print(f"Обратный отсчет: {seconds} секунд")
    while seconds > 0:
        print(f"{seconds} секунд", end='\r', flush=True)
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Время вышло!")
    print("\a")  # Звуковой сигнал (может не работать в некоторых терминалах)

if __name__ == "__main__":
    while True:
        try:
            secs = int(input("Введите количество секунд для обратного отсчета: "))
            if secs < 0:
                print("Введите положительное число.")
                continue
            count_down(secs)
            break
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")