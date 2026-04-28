from task import Task
from storage import load_tasks, save_tasks
from utils import print_tasks, search_tasks, sort_tasks

def add_task(tasks):
    title = input("Назва задачі: ").strip()
    description = input("Опис: ").strip()
    priority = input("Пріоритет (low/medium/high): ").strip().lower()
    if priority not in ["low", "medium", "high"]:
        priority = "medium"
    new_task = Task(title, description, priority)
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Задачу додано!")

def delete_task(tasks):
    try:
        task_id = int(input("ID задачі для видалення: "))
        if 1 <= task_id <= len(tasks):
            tasks.pop(task_id - 1)
            save_tasks(tasks)
            print("🗑️ Видалено!")
        else:
            print("❌ Невірний ID.")
    except ValueError:
        print("❌ Введіть число!")

def mark_done(tasks):
    try:
        task_id = int(input("ID задачі для виконання: "))
        if 1 <= task_id <= len(tasks):
            tasks[task_id - 1].status = "done"
            save_tasks(tasks)
            print("✅ Позначено як виконану!")
        else:
            print("❌ Невірний ID.")
    except ValueError:
        print("❌ Введіть число!")

def edit_task(tasks):
    try:
        task_id = int(input("ID задачі для редагування: "))
        if 1 <= task_id <= len(tasks):
            task = tasks[task_id - 1]
            new_title = input(f"Нова назва ({task.title}): ").strip()
            new_description = input(f"Новий опис ({task.description}): ").strip()
            new_priority = input(f"Новий пріоритет ({task.priority}): ").strip().lower()

            if new_title: task.title = new_title
            if new_description: task.description = new_description
            if new_priority in ["low", "medium", "high"]:
                task.priority = new_priority

            save_tasks(tasks)
            print("✏️ Задачу відредаговано!")
        else:
            print("❌ Невірний ID.")
    except ValueError:
        print("❌ Введіть число!")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Показати всі задачі")
        print("2. Додати задачу")
        print("3. Видалити задачу")
        print("4. Позначити як виконану")
        print("5. Редагувати задачу")
        print("6. Пошук задачі")
        print("7. Сортувати задачі")
        print("8. Вийти")

        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            keyword = input("Введіть ключове слово: ").strip()
            results = search_tasks(tasks, keyword)
            print_tasks(results)
        elif choice == "7":
            sort_by = input("Сортувати за (priority/status): ").strip()
            tasks = sort_tasks(tasks, sort_by)
            print("📊 Відсортовано!")
        elif choice == "8":
            print("👋 Вихід...")
            break
        else:
            print("❌ Невірний вибір!")

if __name__ == "__main__":
    main()
