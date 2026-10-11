# 📝 Week 5 Recap: Data Structures: Dictionaries & Sets

> **สรุปสั้น:** สัปดาห์ที่ 5: dictionary เก็บข้อมูลแบบ key -> value ค้นหาได้เร็ว ส่วน set เก็บเฉพาะค่าที่ไม่ซ้ำ ทำ union / intersection ได้ และฝึกเลือกโครงสร้างข้อมูลให้เหมาะกับงาน

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** Week 5_ Data Structures_ Dictionaries & Sets.docx, p5. Advanced Python Dictionaries.pdf (slides are images), annoucement  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Dictionaries:** Key-value pairs: `{"name": "Alice", "age": 20}`. Keys must be unique and immutable.
- **Safe access:** `d["key"]` raises KeyError if missing; `d.get("key", default)` returns a default instead.
- **Add / change / remove:** `d[k] = v` adds or updates; `del d[k]`, `pop(k)`, `popitem()`, `clear()` remove.
- **Looping:** `for k in d`, `for v in d.values()`, `for k, v in d.items()`. Dictionaries can be nested.
- **Sets:** Unordered, unique items. `set()` makes an empty set (`{}` is an empty dict!). `add`, `remove` (error if missing), `discard` (no error).
- **Set operations:** `|` union, `&` intersection, `-` difference, `^` symmetric difference. Great for removing duplicates and fast membership tests.

## 💻 2. Code snippets

**Contact book with a dictionary**

```python
contacts = {}
contacts["Mint"] = "081-000-0001"      # fake sample numbers
contacts["Beam"] = "081-000-0002"
contacts["Mint"] = "081-000-9999"      # update existing key
print(contacts.get("Ploy", "Not found"))
for name, phone in contacts.items():
    print(f"{name}: {phone}")
```

Output:

```text
Not found
Mint: 081-000-9999
Beam: 081-000-0002
```

**Sets: unique values and comparisons**

```python
python_class = {"Mint", "Beam", "Ploy"}
ai_class = {"Beam", "Nok"}
print("both classes:", python_class & ai_class)
print("all students:", python_class | ai_class)
print("only python:", python_class - ai_class)
print("remove duplicates:", set([1, 2, 2, 3, 3, 3]))
```

Output:

```text
both classes: {'Beam'}
all students: {'Mint', 'Beam', 'Ploy', 'Nok'}
only python: {'Mint', 'Ploy'}
remove duplicates: {1, 2, 3}
```

## ⚠️ 3. Common beginner mistakes

- Using `{}` to make an empty set; it creates an empty dict.
- Using a list as a dict key -> TypeError (lists are mutable).
- Accessing `d["missing"]` without checking -> KeyError; prefer `get()` or `in`.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **AI ethics / privacy:** Dictionaries often hold personal records (name, phone, grades). Collect only what you need (data minimization) and use fake data when testing or prompting AI.
- **Explainable AI:** Dictionaries are readable "feature -> value" records. Many explainability tools present AI decisions exactly this way, e.g. {"income": +0.3, "age": -0.1}.
- **Responsible AI:** Sets help detect duplicate or overlapping data. Duplicate records in a dataset can bias an AI model, so cleaning data is part of responsible AI.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What does `{1, 2, 3} & {2, 3, 4}` return?
2. When is `get()` better than `d[key]`?
3. Which structure would you use for a list of unique tags?

## 🔗 6. Next week

Week 6 packages code into reusable functions and modules.
