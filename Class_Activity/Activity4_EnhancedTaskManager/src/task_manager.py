# src/task_manager.py
"""
โมดูล task_manager.py: Business Logic Layer ของระบบ Enhanced Task Manager
ทำหน้าที่จัดการ collection ของ Task objects, ควบคุมการทำงาน CRUD,
และเป็นพื้นที่ให้นักศึกษาพัฒนาตรรกะสำหรับการค้นหา (Search), การกรอง (Filter), และการจัดเรียง (Sort)
"""

import datetime
try:
    from .task import Task, DueDateTask, PriorityTask
    from .data_persistence import DataPersistence
except ImportError:
    from task import Task, DueDateTask, PriorityTask
    from data_persistence import DataPersistence



class TaskManager:
    """
    คลาสจัดการงาน (Task Manager)
    มุ่งเน้นที่ Business Logic ล้วนๆ ไม่มีการเข้าถึงไฟล์ I/O หรือ CLI Input/Output โดยตรง
    ตามหลักการ Separation of Concerns
    """
    def __init__(self, data_file='data/tasks.json'):
        self.persistence = DataPersistence(data_file)
        self.tasks = self.persistence.load_tasks()
        self.next_id = self._get_next_task_id()

    def _get_next_task_id(self):
        """คำนวณหา ID ลำดับถัดไปที่ไม่ซ้ำกันสำหรับงานใหม่"""
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def _save_changes(self):
        """บันทึกข้อมูลการเปลี่ยนแปลงไปยัง Data Persistence Layer"""
        self.persistence.save_tasks(self.tasks)

    # =========================================================================
    # การดำเนินการ CRUD พื้นฐาน (พร้อมใช้งาน)
    # =========================================================================

    def add_normal_task(self, description, tags=None):
        """เพิ่มงานทั่วไป (Normal Task)"""
        new_task = Task(self.next_id, description, tags=tags)
        self.tasks.append(new_task)
        self.next_id += 1
        self._save_changes()
        return new_task

    def add_due_date_task(self, description, due_date_str, tags=None):
        """เพิ่มงานที่มีวันครบกำหนด (Due Date Task)"""
        new_task = DueDateTask(self.next_id, description, due_date_str, tags=tags)
        self.tasks.append(new_task)
        self.next_id += 1
        self._save_changes()
        return new_task

    def add_priority_task(self, description, priority, tags=None):
        """เพิ่มงานที่มีระดับความสำคัญ (Priority Task)"""
        new_task = PriorityTask(self.next_id, description, priority, tags=tags)
        self.tasks.append(new_task)
        self.next_id += 1
        self._save_changes()
        return new_task

    def get_task_by_id(self, task_id):
        """ค้นหางานตาม ID"""
        return next((task for task in self.tasks if task.id == task_id), None)

    def complete_task(self, task_id):
        """ทำเครื่องหมายว่างานเสร็จสมบูรณ์แล้ว"""
        task = self.get_task_by_id(task_id)
        if task:
            if not task.completed:
                task.mark_complete()
                self._save_changes()
                return True, f"งาน ID {task_id} ถูกเปลี่ยนสถานะเป็น 'เสร็จสมบูรณ์ (Completed)' แล้ว"
            else:
                return False, f"งาน ID {task_id} มีสถานะเสร็จสมบูรณ์อยู่แล้ว"
        return False, f"ไม่พบงาน ID {task_id} ในระบบ"

    def delete_task(self, task_id):
        """ลบงานออกจากระบบตาม ID"""
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) < original_len:
            self._save_changes()
            return True, f"ลบงาน ID {task_id} เรียบร้อยแล้ว"
        return False, f"ไม่พบงาน ID {task_id} ในระบบ"

    def get_all_tasks(self):
        """ส่งคืนรายการงานทั้งหมด"""
        return list(self.tasks)

    # =========================================================================
    # ฟังก์ชันเพิ่มเติมสำหรับนักศึกษาพัฒนาต่อ (Student Assignment Placeholders)
    # =========================================================================

    def search_tasks(self, keyword):
        """
        ค้นหางานตามคำสำคัญ (keyword) ใน description หรือใน tags
        - ไม่สนตัวพิมพ์เล็ก/ใหญ่ (case-insensitive)
        - คืนลิสต์ของ Task objects ที่ตรงเงื่อนไข (ลิสต์ว่างถ้าไม่พบ)
        """
        keyword_lower = keyword.strip().lower()
        if not keyword_lower:
            return []
        return [
            task for task in self.tasks
            if keyword_lower in task.description.lower()
            or any(keyword_lower in tag.lower() for tag in task.tags)
        ]

    def filter_tasks(self, status=None, due_date_before=None, priority=None, tags=None):
        """
        กรองงานตามเงื่อนไข (ทุกเงื่อนไขที่ระบุต้องเป็นจริงพร้อมกัน = AND)

        - status (bool | None): True = เสร็จแล้ว, False = ยังไม่เสร็จ, None = ไม่กรอง
        - due_date_before (str 'YYYY-MM-DD' | datetime.date | None):
              เหลือเฉพาะ DueDateTask ที่ครบกำหนดก่อนหรือตรงกับวันนี้
        - priority (str | None): 'High' / 'Medium' / 'Low' เหลือเฉพาะ PriorityTask ระดับนั้น
        - tags (str | list | None): เหลือเฉพาะงานที่มี tag ตรงกับที่ระบุอย่างน้อย 1 ตัว

        Raises:
            ValueError: ถ้า due_date_before เป็นสตริงที่ไม่ใช่รูปแบบ YYYY-MM-DD
        """
        filtered = list(self.tasks)

        if status is not None:
            filtered = [task for task in filtered if task.completed == status]

        if due_date_before:
            if isinstance(due_date_before, str):
                due_date_obj = datetime.datetime.strptime(due_date_before.strip(), '%Y-%m-%d').date()
            else:
                due_date_obj = due_date_before
            filtered = [
                task for task in filtered
                if isinstance(task, DueDateTask) and task.due_date <= due_date_obj
            ]

        if priority:
            priority_lower = priority.strip().lower()
            filtered = [
                task for task in filtered
                if isinstance(task, PriorityTask) and task.priority.lower() == priority_lower
            ]

        if tags:
            wanted = [tags] if isinstance(tags, str) else list(tags)
            wanted_lower = {tag.strip().lower() for tag in wanted if tag.strip()}
            filtered = [
                task for task in filtered
                if wanted_lower & {tag.lower() for tag in task.tags}
            ]

        return filtered

    # ลำดับความสำคัญ: ตัวเลขน้อย = สำคัญมาก, งานที่ไม่มี priority ไว้ท้ายสุด
    PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}
    VALID_SORT_CRITERIA = ("id", "due_date", "priority")

    def sort_tasks(self, criterion="id", reverse=False):
        """
        จัดเรียงงาน (ไม่แก้ลำดับใน self.tasks คืนลิสต์ใหม่)

        - criterion: "id", "due_date" หรือ "priority" (ค่าอื่นจะใช้ "id")
        - reverse: False = น้อยไปมาก, True = มากไปน้อย
        - งานที่ไม่มี due_date / priority จะอยู่ท้ายรายการเสมอ ไม่ว่าจะเรียงทางไหน
        """
        if criterion not in self.VALID_SORT_CRITERIA:
            criterion = "id"

        if criterion == "id":
            return sorted(self.tasks, key=lambda task: task.id, reverse=reverse)

        if criterion == "due_date":
            with_value = [task for task in self.tasks if isinstance(task, DueDateTask)]
            without_value = [task for task in self.tasks if not isinstance(task, DueDateTask)]
            with_value.sort(key=lambda task: (task.due_date, task.id), reverse=reverse)
        else:  # priority
            with_value = [task for task in self.tasks if isinstance(task, PriorityTask)]
            without_value = [task for task in self.tasks if not isinstance(task, PriorityTask)]
            # reverse=False: High → Low, reverse=True: Low → High
            with_value.sort(key=lambda task: (self.PRIORITY_ORDER.get(task.priority, 99), task.id), reverse=reverse)

        return with_value + sorted(without_value, key=lambda task: task.id)
