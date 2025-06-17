import tkinter as tk
from tkinter import messagebox, simpledialog

class StudentManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("学生管理系统")

        self.students = {}  # 存储学生信息，键为学生ID

        # 创建主框架
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack()

        # 标题
        self.title_label = tk.Label(self.main_frame, text="学生管理系统", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # 按钮
        self.add_button = tk.Button(self.main_frame, text="添加学生", command=self.add_student_gui, width=15)
        self.add_button.grid(row=1, column=0, pady=5, padx=5)

        self.view_button = tk.Button(self.main_frame, text="查看所有学生", command=self.view_students_gui, width=15)
        self.view_button.grid(row=1, column=1, pady=5, padx=5)

        self.find_button = tk.Button(self.main_frame, text="查找学生", command=self.find_student_gui, width=15)
        self.find_button.grid(row=2, column=0, pady=5, padx=5)

        self.delete_button = tk.Button(self.main_frame, text="删除学生", command=self.delete_student_gui, width=15)
        self.delete_button.grid(row=2, column=1, pady=5, padx=5)

        self.exit_button = tk.Button(self.main_frame, text="退出", command=master.quit, width=15, bg="red", fg="white")
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_student_gui(self):
        """添加学生界面的逻辑"""
        dialog = tk.Toplevel(self.master)
        dialog.title("添加学生")
        dialog.transient(self.master)  # 使对话框在主窗口之上
        dialog.grab_set()  # 禁用主窗口直到对话框关闭

        tk.Label(dialog, text="姓名:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(dialog)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(dialog, text="ID:").grid(row=1, column=0, padx=5, pady=5)
        id_entry = tk.Entry(dialog)
        id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(dialog, text="年龄:").grid(row=2, column=0, padx=5, pady=5)
        age_entry = tk.Entry(dialog)
        age_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(dialog, text="年级:").grid(row=3, column=0, padx=5, pady=5)
        grade_entry = tk.Entry(dialog)
        grade_entry.grid(row=3, column=1, padx=5, pady=5)

        def save_student():
            name = name_entry.get().strip()
            student_id = id_entry.get().strip()
            age = age_entry.get().strip()
            grade = grade_entry.get().strip()

            if not all([name, student_id, age, grade]):
                messagebox.showerror("错误", "所有字段都不能为空！", parent=dialog)
                return

            if student_id in self.students:
                messagebox.showerror("错误", f"学生ID {student_id} 已存在。", parent=dialog)
                return

            self.students[student_id] = {
                "name": name,
                "age": age,
                "grade": grade
            }
            messagebox.showinfo("成功", f"学生 {name} (ID: {student_id}) 已添加成功！", parent=dialog)
            dialog.destroy()

        save_button = tk.Button(dialog, text="保存", command=save_student)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def view_students_gui(self):
        """查看所有学生界面的逻辑"""
        if not self.students:
            messagebox.showinfo("信息", "目前没有学生信息。")
            return

        view_window = tk.Toplevel(self.master)
        view_window.title("所有学生信息")
        view_window.transient(self.master)
        view_window.grab_set()

        text_widget = tk.Text(view_window, width=60, height=15, wrap="word")
        text_widget.pack(padx=10, pady=10)

        text_widget.insert(tk.END, "--- 所有学生信息 ---\n")
        for student_id, info in self.students.items():
            text_widget.insert(tk.END, f"ID: {student_id}, 姓名: {info['name']}, 年龄: {info['age']}, 年级: {info['grade']}\n")
        text_widget.insert(tk.END, "--------------------")

        text_widget.config(state="disabled") # 禁止编辑

        close_button = tk.Button(view_window, text="关闭", command=view_window.destroy)
        close_button.pack(pady=5)

    def find_student_gui(self):
        """查找学生界面的逻辑"""
        student_id = simpledialog.askstring("查找学生", "请输入要查找的学生ID:")
        if student_id:
            if student_id in self.students:
                info = self.students[student_id]
                messagebox.showinfo(
                    "学生信息",
                    f"ID: {student_id}\n姓名: {info['name']}\n年龄: {info['age']}\n年级: {info['grade']}"
                )
            else:
                messagebox.showerror("未找到", f"未找到ID为 {student_id} 的学生。")

    def delete_student_gui(self):
        """删除学生界面的逻辑"""
        student_id = simpledialog.askstring("删除学生", "请输入要删除的学生ID:")
        if student_id:
            if student_id in self.students:
                confirm = messagebox.askyesno("确认删除", f"您确定要删除学生ID为 {student_id} 的学生吗？")
                if confirm:
                    name = self.students[student_id]['name']
                    del self.students[student_id]
                    messagebox.showinfo("成功", f"学生 {name} (ID: {student_id}) 已成功删除。")
            else:
                messagebox.showerror("未找到", f"未找到ID为 {student_id} 的学生。")

def main():
    root = tk.Tk()
    app = StudentManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
