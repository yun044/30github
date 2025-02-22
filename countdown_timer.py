import time

def count_down(seconds):
    print(f"Обратный отсчет: {seconds} секунд")
    while seconds:
        print(seconds, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

if __name__ == "__main__":
    try:
        secs = int(input("Введите количество секунд для обратного отсчета: "))
        count_down(secs)
    except ValueError:
        print("Пожалуйста, введите целое число.")


