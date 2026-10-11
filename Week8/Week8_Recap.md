# 📝 Week 8 Recap: OOP Fundamentals & Refactoring the CLI Task Manager

> **สรุปสั้น:** สัปดาห์ที่ 8: เขียนโปรแกรมเชิงวัตถุ (OOP) ด้วย class, object, attribute, method, __init__, self, __str__ / __repr__ แล้วปรับ Task Manager จากสัปดาห์ที่ 7 ให้เป็นคลาส Task และ TaskManager

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 8_ Object-Oriented Programming (OOP) Fundamentals & Refactoring the CLI Task Manager.pdf  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Why OOP:** Procedural code gets messy as apps grow. OOP models real-world things, groups data with behaviour, and improves reuse and maintenance.
- **Core terms:** Class = blueprint; Object = an instance; Attribute = data (`task.description`); Method = function on the object (`task.mark_complete()`).
- **__init__ and self:** `__init__` runs when an object is created and sets its attributes. `self` refers to the current object and is the first parameter of every instance method.
- **Encapsulation:** Keep data and the methods that change it together in one unit.
- **__str__ vs __repr__:** `__str__` gives a friendly text for print(); `__repr__` gives an unambiguous text for developers and debugging.
- **Refactor:** `Task` (id, description, completed, mark_complete, to_dict) and `TaskManager` (tasks list, next_id, add/list/complete/delete, load/save JSON).

## 💻 2. Code snippets

**Task and TaskManager classes**

```python
class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {"id": self.id, "description": self.description,
                "completed": self.completed}

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"[{mark}] {self.id}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                return True
        return False


manager = TaskManager()
manager.add_task("Learn classes")
manager.add_task("Refactor week 7 app")
manager.complete_task(1)
for t in manager.tasks:
    print(t)
print([t.to_dict() for t in manager.tasks])   # ready for json.dump
```

Output:

```text
[x] 1: Learn classes
[ ] 2: Refactor week 7 app
[{'id': 1, 'description': 'Learn classes', 'completed': True}, {'id': 2, 'description': 'Refactor week 7 app', 'completed': False}]
```

## ⚠️ 3. Common beginner mistakes

- Forgetting `self` as the first parameter of a method.
- Writing `description = description` instead of `self.description = description` in __init__.
- Saving objects directly with json.dump; convert with `to_dict()` first.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Explainable AI:** A clear `__str__` / `__repr__` is a small act of explainability: the object can describe its own state. AI systems should likewise be able to explain their state and decisions.
- **Responsible AI:** Encapsulation lets you protect data and add validation (e.g. reject empty descriptions) in one place, which is a basic safety habit for any system that handles user data.
- **AI ethics:** Classes model people and things; choose attributes carefully. Avoid storing sensitive attributes (religion, health, etc.) unless truly required and protected.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What is the difference between a class and an object?
2. When is __init__ called?
3. Why does Task need a to_dict() method?

## 🔗 6. Next week

Week 10 moves to automation and Web APIs, and starts the Final Term Project.
