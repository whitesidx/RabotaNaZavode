import uuid

class Task:
    def __init__(self, title, description, priority="medium", status="todo", task_id=None):
        self.id = task_id if task_id else str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority 
        self.status = status      

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            priority=data.get("priority", "medium"),
            status=data.get("status", "todo"),
            task_id=data["id"]
        )
