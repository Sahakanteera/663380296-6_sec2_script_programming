# 📝 Week 3 Recap: Control Flow: Loops + Advanced: Generators

> **สรุปสั้น:** สัปดาห์ที่ 3: ทำงานซ้ำด้วย for / while, ควบคุม loop ด้วย break / continue, loop ซ้อน และ Generator (yield) ที่ประหยัดหน่วยความจำ รวมถึงการใช้ Kanban / WIP / Changelog กับ learning_log

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 3_ Control Flow_ Loops.docx, p3. Generators.pptx, Week 2 Recap, annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **for loop + range():** `for item in sequence:` repeats for each item. `range(stop)`, `range(start, stop)`, `range(start, stop, step)`; stop is NOT included.
- **while loop:** Repeats while a condition is True. Always have initialization, condition and update, or you get an infinite loop.
- **break / continue:** `break` exits the loop immediately; `continue` skips to the next round.
- **Nested loops:** The inner loop finishes all its rounds for every round of the outer loop (great for tables and grids).
- **Generators (advanced):** A function with `yield` produces values one at a time (lazy). Generator expressions `(x*x for x in data)` use constant memory, unlike list comprehensions. A generator can only be used once.
- **Workflow habits:** Kanban board (To Do / WIP / Done), limit Work-In-Progress, and keep a changelog plus a learning_log.ipynb of AI prompts and responses.

## 💻 2. Code snippets

**Guessing game with while + break**

```python
secret = 7
guesses = [3, 9, 7]          # simulated user inputs
attempts = 0
for guess in guesses:        # in class you would use: while True: guess = int(input(...))
    attempts += 1
    if guess < secret:
        print(guess, "-> Too low")
        continue
    if guess > secret:
        print(guess, "-> Too high")
        continue
    print(guess, "-> Correct! attempts:", attempts)
    break
```

Output:

```text
3 -> Too low
9 -> Too high
7 -> Correct! attempts: 3
```

**Generator: one value at a time**

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a              # pause here and hand back one value
        a, b = b, a + b

print(list(fibonacci(50)))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

total = sum(x * x for x in range(1_000_000))   # generator expression: low memory
print(total)
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
333332833333500000
```

## ⚠️ 3. Common beginner mistakes

- Forgetting to update the counter in a while loop -> infinite loop.
- Expecting `range(1, 10)` to include 10.
- Looping over the same generator twice: the second time it is already empty.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Responsible AI:** Loops automate actions at scale (sending messages, scraping pages). Add limits (max attempts, delays) so your script cannot spam or overload someone else's system.
- **Explainable AI:** Ask the AI to trace a loop step by step (value of each variable per round). Tracing tables are a simple form of explainability.
- **AI ethics:** Kanban + changelog + learning_log make your process transparent and accountable: a reader can see what you did, when, and what AI helped with.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What does `list(range(2, 11, 3))` produce?
2. When would you choose a generator instead of a list?
3. What is the difference between break and continue?

## 🔗 6. Next week

Week 4 stores many values together in lists and tuples.
