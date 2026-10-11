# 📝 Week 10 Recap: Web APIs & JSON, Spreadsheet Automation, Final Project Kick-off

> **สรุปสั้น:** สัปดาห์ที่ 10 (ออนไลน์): ดึงข้อมูลจาก Web API แบบ JSON, ทำ Lab อัตโนมัติกับ spreadsheet และเริ่ม Final Term Project (ต้องมี API, เก็บข้อมูล, รูปแบบ OOP / Functional, test และ CI/CD)

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** 📘 Final Term Project_ Python Application Development.docx, 🍱 Example Project Menu.docx, week 10 announcement and lab titles (the Colab notebook and the Drive folder were not downloaded, so this recap relies on their titles)  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Web APIs & JSON:** Use the `requests` library to call an API (GET / POST), check the status code, handle errors, and parse the JSON response into dicts and lists.
- **Spreadsheet automation (Lab 10):** Basic: read and write Excel / Google Sheets from Python. Advanced: agentic workflows that combine automation steps.
- **Final project requirements:** 1) API integration, 2) data persistence (CSV / JSON / SQLite), 3) functional OR OOP style, 4) unit tests (pytest) + CI/CD pipeline + linting (flake8 / black).
- **Domains:** Allowed: tools, daily apps, data analysis, scientific computing, AI-assisted software, network, health, pet apps. Not recommended: large information systems, finance, government, ERP.
- **Team roles:** Project Manager / CI-CD integrator, Automated Tester & QA, Core Developer(s); solo students rotate roles.
- **Process:** Project pitch, then Sprint 1, 2, 3 and a final presentation, with a GitHub repo split by sprint and a matching changelog.

## 💻 2. Code snippets

**Processing an API-style JSON response**

```python
import json

# A response like the ones you get from requests.get(url).json()
raw = '{"city": "Khon Kaen", "temp_c": 31.5, "aqi": 72}'
data = json.loads(raw)
print(f"{data['city']}: {data['temp_c']} °C, AQI {data['aqi']}")

# With a real API (needs internet):
# import requests
# r = requests.get("https://api.example.com/weather", params={"q": "Khon Kaen"}, timeout=10)
# r.raise_for_status()      # stop with a clear error on 4xx / 5xx
# data = r.json()
```

Output:

```text
Khon Kaen: 31.5 °C, AQI 72
```

**A first unit test (pytest style)**

```python
def bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError("height must be positive")
    return round(weight_kg / height_m ** 2, 1)

def test_bmi():
    assert bmi(60, 1.70) == 20.8

test_bmi()            # pytest finds and runs test_* functions automatically
print("test passed")
```

Output:

```text
test passed
```

## ⚠️ 3. Common beginner mistakes

- Putting API keys directly in code pushed to GitHub; use environment variables and .gitignore.
- Not setting a timeout or checking the status code, so the app hangs or crashes.
- Choosing a project that is too big (ERP, banking); keep scope small and testable.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Responsible AI:** Respect API terms of use and rate limits, and credit your data sources. For AI-assisted projects (sentiment analysis, chatbots), state the model's limits to users.
- **Explainable AI:** If your project uses an AI model, show users why it made a prediction (e.g. which words made a review "negative") and how confident it is.
- **AI ethics:** Health and personal data need extra care: use mock data, ask for consent, and avoid giving medical or financial advice. That is one reason finance and government apps are excluded.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. What are the 4 core requirements of the final project?
2. Why call `raise_for_status()` after a request?
3. Where should you keep API keys?

## 🔗 6. Next week

Week 11 automates PDFs and Word documents and moves the final project into Sprint 1.
