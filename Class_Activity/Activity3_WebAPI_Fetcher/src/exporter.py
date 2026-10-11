"""
src/exporter.py
[Task 3] ฟังก์ชันบันทึกข้อมูลที่ดึงจาก API ลงไฟล์ JSON
"""

import json
import os
from typing import Any

# โฟลเดอร์เก็บไฟล์ที่ export (อยู่ข้าง main.py)
EXPORT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "exports")


def export_to_json_file(filename: str, data: Any) -> bool:
    """
    บันทึก data (dict หรือ list) ลงไฟล์ JSON ในโฟลเดอร์ exports/

    - ใช้ encoding='utf-8' + ensure_ascii=False เพื่อให้ภาษาไทยอ่านออก
    - ใช้ indent=4 ให้ไฟล์อ่านง่าย
    - ตัดส่วน path ออกจากชื่อไฟล์ (os.path.basename) กันการเขียนไฟล์ออกนอกโฟลเดอร์ exports
    - ดักจับ PermissionError / OSError / TypeError ไม่ให้โปรแกรมแครช

    :return: True หากบันทึกสำเร็จ, False หากล้มเหลว
    """
    safe_name = os.path.basename(filename.strip()) or "exported_data.json"
    if not safe_name.lower().endswith(".json"):
        safe_name += ".json"
    file_path = os.path.join(EXPORT_DIR, safe_name)

    try:
        os.makedirs(EXPORT_DIR, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ บันทึกไฟล์สำเร็จ: {file_path}")
        return True
    except PermissionError:
        print(f"❌ ไม่มีสิทธิ์เขียนไฟล์: {file_path}")
    except TypeError as e:
        print(f"❌ ข้อมูลบางส่วนแปลงเป็น JSON ไม่ได้: {e}")
    except OSError as e:
        print(f"❌ เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")
    return False
