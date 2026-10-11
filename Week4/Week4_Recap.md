# 📝 Week 4 Recap: Data Structures: Lists & Tuples

> **สรุปสั้น:** สัปดาห์ที่ 4: เก็บข้อมูลหลายค่าด้วย list (แก้ไขได้) และ tuple (แก้ไขไม่ได้) เรียน indexing, slicing, method ของ list และเริ่มคิดหัวข้อ mini project

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 4_ Data Structures_ Lists & Tuples.docx, p7. List.pptx, Sequence of AI Prompts.docx, annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Lists:** Ordered, mutable (changeable), allow duplicates, written with `[]`.
- **Indexing & slicing:** `lst[0]` is the first item, `lst[-1]` the last. `lst[start:end:step]` makes a new list; end is not included.
- **List methods:** Add: `append`, `insert`, `extend`. Remove: `remove`, `pop`, `del`, `clear`. Other: `len`, `sort` (in place) vs `sorted` (new list), `reverse`, `count`, `index`.
- **Tuples:** Ordered, immutable, written with `()`. A one-item tuple needs a comma: `("apple",)`. Changing a tuple raises TypeError.
- **When to use which:** Tuple for fixed data (coordinates, records, dict keys); list for data that grows or changes. Convert with `list()` and `tuple()`.
- **Advanced list tricks:** `any()` / `all()`, `zip()`, copying (`lst.copy()` vs `=`), removing duplicates, sorting with `key=`.

## 💻 2. Code snippets

**List operations**

```python
students = ["Mint", "Beam", "Ploy"]
students.append("Nok")
students.insert(0, "Arm")
students.remove("Beam")
print(students, len(students))
print(students[0], students[-1], students[1:3])
print(sorted(students))      # new sorted list, original unchanged
if "Ploy" in students:
    print("Ploy is at index", students.index("Ploy"))
```

Output:

```text
['Arm', 'Mint', 'Ploy', 'Nok'] 4
Arm Nok ['Mint', 'Ploy']
['Arm', 'Mint', 'Nok', 'Ploy']
Ploy is at index 2
```

**Tuples are immutable**

```python
point = (3, 4)
x, y = point                 # tuple unpacking
print("distance from origin:", (x**2 + y**2) ** 0.5)
try:
    point[0] = 10
except TypeError as err:
    print("Cannot change a tuple:", err)

a = [1, 2, 3]
b = a            # same list, two names
c = a.copy()     # a real, separate copy
a.append(4)
print(b, c)      # [1, 2, 3, 4] [1, 2, 3]
```

Output:

```text
distance from origin: 5.0
Cannot change a tuple: 'tuple' object does not support item assignment
[1, 2, 3, 4] [1, 2, 3]
```

## ⚠️ 3. Common beginner mistakes

- `b = a` does NOT copy a list; both names point to the same list. Use `a.copy()`.
- `x = lst.sort()` sets x to None. Use `sorted(lst)` if you need the result.
- `("apple")` is just a string; you need `("apple",)` for a tuple.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **AI ethics / privacy:** Lists of students or users are personal data. Use fake names in examples and never upload real class lists to an AI tool.
- **Responsible AI:** When asking AI for mini project ideas (this week's prompt), check that the idea solves a real problem and does not collect data it does not need.
- **Explainable AI:** Choosing tuple vs list is a design decision. Write a short comment explaining WHY you chose it; explaining choices is a core habit of explainable systems.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What is `[10, 20, 30, 40][1:3]`?
2. Why can a tuple be a dictionary key but a list cannot?
3. What is the difference between `sort()` and `sorted()`?

## 🔗 6. Next week

Week 5 introduces dictionaries (key -> value) and sets (unique items).
