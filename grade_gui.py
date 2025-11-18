import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        m1 = float(sub1_entry.get())
        m2 = float(sub2_entry.get())
        m3 = float(sub3_entry.get())

        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        total_label.config(text=f"Total Marks: {total}")
        avg_label.config(text=f"Average: {avg:.2f}")
        grade_label.config(text=f"Grade: {grade}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric marks!")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("420x450")
root.config(bg="#f0f4f7")

title = tk.Label(root, text="🎓 Student Grade Calculator", 
                 font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#333")
title.pack(pady=20)

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
frame.pack(pady=10, padx=20)

tk.Label(frame, text="Subject 1 Marks:", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
sub1_entry = tk.Entry(frame, font=("Arial", 14), width=10)
sub1_entry.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Subject 2 Marks:", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
sub2_entry = tk.Entry(frame, font=("Arial", 14), width=10)
sub2_entry.grid(row=1, column=1, padx=10)

tk.Label(frame, text="Subject 3 Marks:", font=("Arial", 14), bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
sub3_entry = tk.Entry(frame, font=("Arial", 14), width=10)
sub3_entry.grid(row=2, column=1, padx=10)
calc_btn = tk.Button(root, text="Calculate Grade", 
                     font=("Arial", 16, "bold"),
                     bg="#4CAF50", fg="white", width=20, command=calculate_grade)
calc_btn.pack(pady=20)
total_label = tk.Label(root, text="Total Marks: ", font=("Arial", 14), bg="#f0f4f7")
total_label.pack()

avg_label = tk.Label(root, text="Average: ", font=("Arial", 14), bg="#f0f4f7")
avg_label.pack()

grade_label = tk.Label(root, text="Grade: ", font=("Arial", 16, "bold"), fg="#333", bg="#f0f4f7")
grade_label.pack(pady=10)

root.mainloop()
