# 📝 Week 7 Recap: Building a Simple CLI Application, Error Handling & Project Structure

> **สรุปสั้น:** สัปดาห์ที่ 7: นำเสนอ mini project และรวมความรู้ทั้งหมดมาสร้างแอป Task Manager แบบ command line จัดโครงสร้างโปรเจกต์ จัดการ error ด้วย try-except บันทึกข้อมูลเป็น JSON ใช้ debugger และ Git / GitHub

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 7_ Building a Simple CLI Application, Error Handling & Project Structure.pdf, week 7 mini project post  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Review weeks 1-6:** Data types + control flow + data structures + functions, combined to build something useful.
- **CLI design:** A main `while True` loop that shows a menu, reads a command and calls functions.
- **Project structure:** `main.py` (entry point), `src/` (task_data.py for saving/loading, task_logic.py for add/list/complete/delete), `data/tasks.json`, `README.md`, `.gitignore`.
- **Error handling:** `try` / `except` catches errors such as ValueError, KeyError, IndexError, FileNotFoundError. Optional `else` (no error) and `finally` (always runs). Catch specific errors, not everything.
- **JSON persistence:** `with open(...) as f:` closes the file for you. `json.dump(data, f)` saves, `json.load(f)` loads lists and dicts.
- **Debugging & Git:** VS Code breakpoints, Step Over (F10) / Into (F11) / Out, watching variables. Git: `init`, `add`, `commit -m`, `remote add`, `push`.

## 💻 2. Code snippets

**Safe number input with try-except**

```python
def parse_task_id(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a valid number, please try again.")
        return None

print(parse_task_id("3"), parse_task_id("abc"))
```

Output:

```text
'abc' is not a valid number, please try again.
3 None
```

**Save and load tasks as JSON**

```python
import json, os

tasks = [{"id": 1, "description": "Read week 7 notes", "completed": False}]

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(tasks, f, ensure_ascii=False, indent=2)

try:
    with open("tasks.json", encoding="utf-8") as f:
        loaded = json.load(f)
except FileNotFoundError:
    loaded = []
print(loaded)
os.remove("tasks.json")      # clean up the demo file
```

Output:

```text
[{'id': 1, 'description': 'Read week 7 notes', 'completed': False}]
```

## ⚠️ 3. Common beginner mistakes

- Bare `except:` that hides every error, including your own bugs.
- Forgetting `encoding="utf-8"`, so Thai text breaks in JSON files.
- Committing data files or secrets (API keys) to GitHub; list them in .gitignore.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Responsible AI:** "Errors should never pass silently": show users clear, honest error messages instead of crashing or hiding problems. Trustworthy software, including AI apps, fails gracefully.
- **AI ethics / privacy:** Data saved to JSON stays on disk. Store only what you need, and never push personal data or API keys to a public repo.
- **Explainable AI:** Git history and changelogs explain how and why code changed. Write meaningful commit messages, and note when code was AI-assisted.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. Which exception does `int("abc")` raise?
2. Why is `with open(...)` preferred over open/close?
3. What should go into .gitignore?

## 🔗 6. Next week

Week 8 refactors this Task Manager with Object-Oriented Programming (classes).
