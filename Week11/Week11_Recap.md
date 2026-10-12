# 📝 Week 11 Recap: Automating PDFs & Word Documents, Project Planning & Design

> **สรุปสั้น:** สัปดาห์ที่ 11: ใช้ Python อ่าน/สร้าง/แก้ไขไฟล์ PDF และ Word อัตโนมัติ (LabX BASIC Document Automator และ ADV Document Agent) พร้อมวางแผนและออกแบบ Final Project (Enhanced Task Manager) เข้าสู่ Sprint 1

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** 📘 LabX BASIC Document Automator, LabX ADV Week 11: Document Agent (my repo Week11/Week11_LabADV_DocumentAgent), Class Activity 4 design doc (enhanced-task-manager-design)  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Reading PDFs:** Use `pypdf` (`PdfReader`) to open a PDF, loop over `reader.pages`, and call `page.extract_text()`. Scanned PDFs have no text layer and need OCR.
- **Creating / editing PDFs:** Merge, split, or rotate pages with `PdfWriter`; generate new PDFs (reports, certificates) with a library such as `reportlab` or `fpdf2`.
- **Word documents:** `python-docx`: `Document()` to create, `add_heading`, `add_paragraph`, `add_table`, then `save()`. Open an existing .docx to read `doc.paragraphs` or fill a template.
- **Template filling:** Keep a template with placeholders such as {name} and fill them from data (CSV / JSON / dict) to produce many documents at once (mail-merge).
- **Document agent (ADV):** Chain steps into a pipeline: read input -> extract fields -> decide what to do (rules or AI) -> write output files -> log every action so it can be checked.
- **Project planning (Sprint 1):** Write the project scope, user stories, data model (Task: title, status, priority, due_date, tags), module layout (models / storage / services / cli), and a test plan before coding.

## 💻 2. Code snippets

**Mail-merge with a template (same idea as filling a .docx)**

```python
from string import Template

template = Template("Dear $name,\nYour grade for $course is $grade.\n")
students = [
    {"name": "Ann", "course": "CP352301", "grade": "A"},
    {"name": "Ben", "course": "CP352301", "grade": "B+"},
]
for s in students:
    print(template.substitute(s))

# With python-docx (pip install python-docx):
# from docx import Document
# doc = Document(); doc.add_heading("Grade Report", 1)
# doc.add_paragraph(template.substitute(s)); doc.save(f"{s['name']}.docx")
```

Output:

```text
Dear Ann,
Your grade for CP352301 is A.

Dear Ben,
Your grade for CP352301 is B+.
```

**Extracting fields from document text**

```python
import re

# Text you might get from PdfReader(...).pages[0].extract_text()
text = """Invoice No: INV-2026-014
Date: 2026-10-05
Total: 1,250.00 THB"""

invoice = re.search(r"Invoice No:\s*(\S+)", text).group(1)
total = float(re.search(r"Total:\s*([\d,.]+)", text).group(1).replace(",", ""))
print(invoice, total)
```

Output:

```text
INV-2026-014 1250.0
```

**A simple data model for the project (dataclass)**

```python
from dataclasses import dataclass, field, asdict

@dataclass
class Task:
    title: str
    priority: str = "medium"
    status: str = "todo"
    tags: list = field(default_factory=list)

t = Task("Write Sprint 1 plan", priority="high", tags=["project"])
print(asdict(t))
```

Output:

```text
{'title': 'Write Sprint 1 plan', 'priority': 'high', 'status': 'todo', 'tags': ['project']}
```

## ⚠️ 3. Common beginner mistakes

- Expecting `extract_text()` to work on scanned PDFs; it returns empty text without OCR.
- Overwriting the original file instead of saving the result as a new file.
- Hard-coding file paths like C:/Users/...; use `pathlib.Path` and paths relative to the project.
- Starting to code the final project with no plan, data model, or test cases.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Responsible AI:** A document agent can read contracts, invoices, or personal records. Process only files you are allowed to use, keep the originals, and let a human review the output before it is sent.
- **Explainable AI:** Log which rule or which extracted field led to each decision (e.g. "total > 1000 -> flagged") so the result can be checked and explained.
- **AI ethics:** Documents often contain personal data (names, ID numbers). Mask or remove what you do not need, and never upload private documents to public AI tools.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. Why can extract_text() return an empty string?
2. How does mail-merge reduce repeated work?
3. What should go in a Sprint 1 plan before writing code?

## 🔗 6. Next week

Week 12 automates email and SMS and continues developing the final project.
