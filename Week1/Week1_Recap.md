# 📝 Week 1 Recap: Introduction to Python & Basic Syntax

> **สรุปสั้น:** สัปดาห์แรก: รู้จักวิชาและภาษา Python ติดตั้งเครื่องมือ (VS Code / Anaconda / Colab) และเรียนพื้นฐาน print(), ตัวแปร, ชนิดข้อมูล และ input()

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** 1. Introduction - SP.pptx, 2. Getting Strarted.pptx, 3. Week 1_ Introduction to Python & Basic Syntax.docx, annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Why Python for scripting:** High-level, interpreted, readable (almost like pseudo-code). Used for automation, web, data analysis and AI/ML.
- **Zen of Python:** Run `import this`. Key ideas: Readability counts; Explicit is better than implicit; Errors should never pass silently.
- **Setting up:** Local: VS Code or Anaconda, check with `python --version`. Cloud: Google Colab notebook. Ways to run: REPL (`>>>`), `python hello.py`, `python -c '...'`.
- **Variables & data types:** Python uses dynamic typing. Basic types: int, float, str, bool. Use snake_case names; names are case-sensitive and cannot be keywords.
- **Input / Output:** `print()` shows output. `input()` ALWAYS returns a str, so convert with `int()` / `float()` before doing math.

## 💻 2. Code snippets

**Variables and types**

```python
age = 20              # int
price = 19.99         # float
name = "Alice"        # str
is_student = True     # bool
print(name, "is", age, "years old")
print(type(age), type(price), type(name), type(is_student))
```

Output:

```text
Alice is 20 years old
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
```

**input() returns a string**

```python
# input() is simulated here so the snippet runs anywhere
age_text = "20"              # what input("Enter your age: ") would give you
age = int(age_text)          # convert before doing math
print("In 5 years you will be", age + 5)
print("Without converting:", age_text + "5")   # string joining, not math!
```

Output:

```text
In 5 years you will be 25
Without converting: 205
```

## ⚠️ 3. Common beginner mistakes

- Forgetting that `input()` returns text: `"20" + 5` raises a TypeError.
- Mixing tabs and spaces or wrong indentation -> IndentationError.
- Using a keyword (e.g. `class`, `for`) as a variable name -> SyntaxError.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Explainable AI:** When an AI assistant gives you code, ask it to explain each line. If you cannot explain the code yourself, you have not learned it yet (Zen: "If the implementation is hard to explain, it's a bad idea").
- **Responsible AI:** Use GenAI (Gemini, ChatGPT, Copilot...) for learning, but follow the course's academic integrity rules: share ideas, do not copy-paste other students' code.
- **AI ethics:** Never paste personal data (student ID, passwords, real names of others) into an AI chat. Use fake sample data like "Alice".

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What does `type(3.0)` return?
2. Why must you use `int()` after `input()` when calculating age?
3. Name two ways to run a Python script.

## 🔗 6. Next week

Week 2 teaches programs to make decisions with if / elif / else, plus a first look at list comprehensions.
