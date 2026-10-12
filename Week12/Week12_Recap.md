# 📝 Week 12 Recap: Automating Communications (Email & SMS), Final Project Development

> **สรุปสั้น:** สัปดาห์ที่ 12: ส่งและอ่านอีเมลอัตโนมัติด้วย smtplib / imaplib, ส่ง SMS (ผ่าน email-to-SMS gateway หรือ API), ทำ Agentic Communication Automator และพัฒนา Final Project (Enhanced Task Manager) ต่อพร้อม test

**วิชา:** CP352301 Script Programming (1/2569)  
**แหล่งข้อมูล:** 📘 LabX BASIC Email & SMS, LabX ADV Agentic Communication Automator (my repo Week12/Week12_LabADV_AgenticCommAutomator), Lab 12 Final Project – Enhanced Task Manager (Week12/Week12_Lab12_FinalProject)  
**เวลาอ่าน:** ~5 นาที

*AI Co-Learner Prelude: "As a Python novice, please respond with AI ethics, explainable AI, and responsible AI in mind."*

---

## 🎯 1. What we learned

- **Building an email:** `email.message.EmailMessage`: set From / To / Subject, `set_content()` for the body, and `add_attachment()` for PDF / Excel files.
- **Sending (SMTP):** `smtplib.SMTP_SSL('smtp.gmail.com', 465)` then `login()` with an App Password (not your real password) and `send_message()`.
- **Reading (IMAP):** `imaplib.IMAP4_SSL`, `select('INBOX')`, `search(None, 'FROM', '"x@y.com"')`, `fetch()`; quote values that contain spaces, and retry because new mail can take time to arrive.
- **SMS:** Send through an email-to-SMS gateway address or an SMS API (e.g. Twilio); keep messages short and include only what is necessary.
- **Agentic automator (ADV):** Rules in a config file decide the action (reply, forward, SMS alert); every match, message, and reply is written to an audit log; secrets come from .env.
- **Final project (Lab 12):** Enhanced Task Manager: search, filter (AND logic), and sort (tasks with no value stay last), with input validation in the CLI and pytest tests.

## 💻 2. Code snippets

**Building an email without sending it**

```python
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "me@example.com"
msg["To"] = "teacher@example.com"
msg["Subject"] = "Weekly report"
msg.set_content("Hello,\nThe weekly report is attached.\n")
msg.add_attachment(b"col1,col2\n1,2\n", maintype="text",
                   subtype="csv", filename="report.csv")
print(msg["Subject"], "->", msg["To"], "| parts:", len(msg.get_payload()))

# To send (needs internet and an App Password from .env):
# import smtplib, os
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
#     s.login(os.environ["SENDER_EMAIL"], os.environ["APP_PASSWORD"])
#     s.send_message(msg)
```

Output:

```text
Weekly report -> teacher@example.com | parts: 2
```

**Rule-based actions with an audit log**

```python
from datetime import datetime

rules = [{"if_subject_has": "urgent", "action": "sms"},
         {"if_subject_has": "invoice", "action": "reply"}]
audit = []

def handle(subject):
    for r in rules:
        if r["if_subject_has"] in subject.lower():
            audit.append((datetime.now().strftime("%H:%M:%S"), subject, r["action"]))
            return r["action"]
    return "ignore"

for s in ["URGENT: server down", "Invoice #14", "Lunch?"]:
    print(s, "->", handle(s))
print(len(audit), "actions logged")
```

Output:

```text
URGENT: server down -> sms
Invoice #14 -> reply
Lunch? -> ignore
2 actions logged
```

**Sorting so empty values stay last**

```python
tasks = [{"t": "A", "due": "2026-10-20"}, {"t": "B", "due": None},
         {"t": "C", "due": "2026-10-15"}]
done = sorted([x for x in tasks if x["due"]], key=lambda x: x["due"], reverse=True)
result = done + [x for x in tasks if not x["due"]]
print([x["t"] for x in result])
```

Output:

```text
['A', 'C', 'B']
```

## ⚠️ 3. Common beginner mistakes

- Putting the Gmail App Password in code or pushing .env to GitHub; keep it in .env and add .env to .gitignore.
- Searching IMAP with an unquoted value that contains spaces, which causes a search error.
- Checking the inbox once right after sending; mail can take seconds to arrive, so wait and retry.
- Sending automated messages to real people while testing; use your own test addresses.

## 🤖 4. AI ethics · Explainable AI · Responsible AI

- **Responsible AI:** Automated messages reach real people. Limit who the bot may contact, add rate limits, and keep a human able to stop it (dry-run mode, confirmation before sending).
- **Explainable AI:** The audit log records which rule triggered each email or SMS, so anyone can see why a message was sent.
- **AI ethics:** Do not send spam or messages people did not agree to receive, protect email addresses and phone numbers, and make it clear when a reply is automated.

## ✅ 5. Self-check (ลองตอบเองก่อนใช้ AI)

1. Why use an App Password instead of your Gmail password?
2. What does the audit log help you explain?
3. Why should tasks without a due date stay at the end after sorting?

## 🔗 6. Next week

Weeks 13–15 continue the final project sprints, testing, CI/CD, and the final presentation.
