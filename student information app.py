import tkinter as tk
from tkinter import messagebox

class StudentInformationApp:
    def __init__(self,root):
        self.student = []
        self.root = root
        self.root.title("Student Information App")
        self.create_widget()

    def create_widget(self):
        tk.Label(self.root , text="name").pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        tk.Label(self.root, text="rollno").pack(pady=5)
        self.rollno_entry = tk.Entry(self.root)
        self.rollno_entry.pack(pady=5)
        tk.Label(self.root, text="marks").pack(pady=5)
        self.marks_entry = tk.Entry(self.root)
        self.marks_entry.pack(pady=5)

        tk.Button(self.root , text = "ADD" , command=self.add_number).pack(pady=5)
        tk.Button(self.root , text="REMOVE" , command=self.remove_number).pack(pady=5)
        tk.Button(self.root , text="DISPLAY" , command=self.display_number).pack(pady=5)
        tk.Button(self.root , text="TOTAL" , command=self.total_number).pack(pady=5)

        self.display = tk.Text(self.root)
        self.display.pack(pady=5)



    def add_number(self):
        name = self.name_entry.get()
        rollno = self.rollno_entry.get()
        try:
            marks = float(self.marks_entry.get())
        except ValueError:
            messagebox.showerror("invalid" , "enter valid marks")
            return
        if not name or not rollno :
            messagebox.showerror("invalid" , "name or rollno should not be empty")
            return
        self.student.append({"name":name , "rollno": rollno , "marks": marks })
        messagebox.showinfo("Success", "Student added successfully!")
        self.clear_entries()

    def remove_number(self):
        name = self.name_entry.get().strip()  # Strip to remove leading/trailing spaces
        if not name:
            messagebox.showerror("Invalid Input", "Please enter a name to remove.")
            return

        for student in self.student:
            if student["name"] == name:
                self.student.remove(student)
                messagebox.showinfo("Success", f"Successfully removed {name}.")
                self.clear_entries()
                return

        messagebox.showerror("Error", f"{name} not found.")

    def display_number(self):
        self.display.delete("1.0" , tk.END)
        if not self.student:
            self.display.insert(tk.END , "name not found.\n")
        else:
            for student in self.student:
                self.display.insert(tk.END , f"name: {student['name']} , rollno: {student['rollno']} , marks: {student['marks']:.2f}.\n")

    def total_number(self):
        messagebox.showinfo("total student" , f"total number of student : {len(self.student)}")

    def clear_entries(self):
        self.name_entry.delete(0 , tk.END)
        self.rollno_entry.delete(0 , tk.END)
        self.marks_entry.delete(0 , tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentInformationApp(root)
    root.mainloop()

