# 📝 Week 2 Recap: Control Flow: Conditionals + Lecture: List Comprehension

> **สรุปสั้น:** สัปดาห์ที่ 2: ให้โปรแกรมตัดสินใจด้วย if / elif / else ใช้ตัวดำเนินการเปรียบเทียบและตรรกะ และเรียน List Comprehension (สร้าง list แบบบรรทัดเดียว)

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 2_ Control Flow_ Conditionals.docx, p2. List Comprehention.pptx, Week2_Snapshot.docx, annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Relational operators:** `==  !=  <  >  <=  >=` compare values and give True/False. String comparison is case-sensitive ("python" != "Python").
- **Logical operators:** `and` (both True), `or` (at least one True), `not` (flip the value).
- **if / elif / else:** Python checks from top to bottom and runs ONLY the first True branch, so the order of conditions matters. Indentation defines each block.
- **Nested conditionals:** An if inside another if. Useful, but too much nesting hurts readability ("Flat is better than nested").
- **List comprehension (lecture):** `[expression for item in iterable if condition]` builds a new list in one line. It is like a for-loop with `.append()`, but shorter and usually faster.
- **Comprehension tips:** if/else that CHANGES values goes before `for`; `if` that FILTERS goes after. Don't use comprehensions for side effects like `print()`; `list.sort()` returns None, use `sorted()`.

## 💻 2. Code snippets

**if / elif / else: a grading scale**

```python
score = 84.5
if score >= 90:
    grade = "A"
elif score >= 80:      # first True condition -> Python stops checking here
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)   # Grade: B
```

Output:

```text
Grade: B
```

**List comprehension vs. for-loop**

```python
# for-loop version
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)                       # [1, 4, 9, 16, 25]

# same result as a list comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# filter: only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)                         # [0, 2, 4, 6, 8]

# transform with if/else (goes BEFORE for)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)
```

Output:

```text
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]
[0, 2, 4, 6, 8]
['even', 'odd', 'even', 'odd', 'even']
```

## ⚠️ 3. Common beginner mistakes

- Using `=` (assign) instead of `==` (compare) in a condition.
- Putting a broader condition first (`score >= 70` before `score >= 90`) so later branches never run.
- Writing `[x for x in data else 0]`: else is only allowed in the expression part, before `for`.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Explainable AI:** if/elif rules are "white-box" logic: anyone can read why a decision was made. Real AI models are often black boxes, which is why we need explainability. Practise by printing WHY your program chose a branch.
- **AI ethics / fairness:** Conditions encode rules about people (age limits, discounts, grades). Ask: is this threshold fair? Who could be treated unfairly by this rule?
- **Responsible AI:** Keep a learning_log.ipynb: record the prompt you used, the AI's answer, and what you checked or changed. That makes your use of AI transparent.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What prints if `temp = 25` and `is_raining = True` in the picnic example?
2. Rewrite `[x*2 for x in nums if x > 0]` as a normal for-loop.
3. Why is `[print(x) for x in data]` considered bad style?

## 🔗 6. Next week

Week 3 adds loops (for / while, break / continue) and generators, which handle large data without filling memory.
