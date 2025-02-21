import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Задача '{description}' добавлена!")



def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Список задач пуст!")
        return
    print("\n📌 Список дел:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {status} {task['task']}")



def complete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Задача {task_number} выполнена!")
    else:
        print("❌ Неверный номер задачи.")



def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Задача '{removed_task['task']}' удалена!")
    else:
        print("❌ Неверный номер задачи.")



def main():
    while True:
        print(
            "\n📋 Меню:\n1. Добавить задачу\n2. Показать задачи\n3. Отметить задачу как выполненную\n4. Удалить задачу\n5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            desc = input("Введите описание задачи: ")
            add_task(desc)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_tasks()
            num = int(input("Введите номер выполненной задачи: "))
            complete_task(num)
        elif choice == "4":
            show_tasks()
            num = int(input("Введите номер задачи для удаления: "))
            delete_task(num)
        elif choice == "5":
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()