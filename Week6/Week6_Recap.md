# 📝 Week 6 Recap: Functions & Modules

> **สรุปสั้น:** สัปดาห์ที่ 6 (เรียนชดเชยออนไลน์): เขียนฟังก์ชันด้วย def, parameter / argument, return, scope ของตัวแปร (LEGB), lambda และการ import module เช่น math, random พร้อมเริ่มทำ mini project

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 6_ Functions & Modules.docx, p6. Functions.pptx, annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Why functions:** DRY (Don't Repeat Yourself): organize, reuse, and debug code more easily. Define with `def name(params):` and document with a docstring.
- **Parameters & arguments:** Positional, keyword (`key=value`), default values, `*args` (many positional) and `**kwargs` (many keyword).
- **Return values:** `return` sends a value back and exits the function. No return means it returns None. Returning several values gives a tuple.
- **Scope (LEGB):** Local -> Enclosing -> Global -> Built-in. Prefer passing parameters and returning values over `global`.
- **Advanced (p6):** Lambda (small anonymous functions), recursion, closures, and the mutable default argument trap (`def f(x=[])`).
- **Modules:** A .py file of reusable code. `import math`, `import random as rnd`, `from math import sqrt`. Avoid `from x import *`.

## 💻 2. Code snippets

**Function with docstring, default value and error handling**

```python
def divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
        return None
    return a / b

def power(base, exponent=2):
    """Return base to the power of exponent (default: square)."""
    return base ** exponent

print(divide(10, 4), divide(1, 0))
print(power(5), power(2, exponent=10))
```

Output:

```text
2.5 None
25 1024
```

**Modules and the mutable-default trap**

```python
import math
import random

print(math.sqrt(16), round(math.pi, 2))
random.seed(42)                       # fixed seed = reproducible result
print(random.randint(1, 6))

def add_item(item, basket=None):      # NOT basket=[]
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("apple"), add_item("banana"))   # ['apple'] ['banana']
```

Output:

```text
4.0 3.14
6
['apple'] ['banana']
```

## ⚠️ 3. Common beginner mistakes

- Printing inside a function instead of returning the value, so the caller cannot use it.
- Using a mutable default like `def f(items=[])`; the list is shared between calls.
- Overusing `global`, which makes code hard to test and explain.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Explainable AI:** A good docstring says what goes in, what comes out, and what can go wrong. Clear function contracts make any system, including AI pipelines, easier to explain and audit.
- **Responsible AI:** Randomness: setting `random.seed()` makes results reproducible. Reproducibility is a key requirement for trustworthy AI experiments.
- **AI ethics:** When AI writes a function for you, test it with edge cases (0, negative, empty) before trusting it. You remain responsible for code you submit.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What does a function return if it has no return statement?
2. Why is `def f(x=[])` dangerous?
3. What is the difference between `import math` and `from math import sqrt`?

## 🔗 6. Next week

Week 7 combines everything into a CLI application with error handling, JSON files and Git.
