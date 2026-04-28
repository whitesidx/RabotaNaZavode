def print_tasks(tasks):
    if not tasks:
        print("Список задач порожній.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"[{i}] {task.title} ({task.priority}) - {task.status}")

def search_tasks(tasks, keyword):
    results = [t for t in tasks if keyword.lower() in t.title.lower() or keyword.lower() in t.description.lower()]
    return results

def sort_tasks(tasks, by="priority"):
    if by == "priority":
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(tasks, key=lambda t: priority_order.get(t.priority, 2))
    elif by == "status":
        return sorted(tasks, key=lambda t: t.status)
    else:
        return tasks
