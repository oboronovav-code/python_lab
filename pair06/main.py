import students_utils
import tkinter as tk

students = ["Alice", "Bob", "Charlie", "David"]

def cmn_check(students):
    try:
        value = int(entry.get())
        if value < 1 or value > 20:
            raise ValueError("Кількість оцінок повинна бути від 1 до 20.")

        for student in students:
            grades = students_utils.generate_grades(value)
            average = students_utils.average_grade(grades)
            level = students_utils.get_level(average)
            print(f"{student}: {grades} \n Average: {average:.2f} \n Level: {level}")

            text.delete("1.0", tk.END)
            text.insert(tk.END, f"{student}: {grades} \n Average: {average:.2f} \n Level: {level}\n")
    except ValueError as e:
        text.delete("1.0", tk.END)
        text.insert(tk.END, f"Помилка: {e}")

window = tk.Tk()
window.title("статистика учнів")
window.geometry("800x600")

label = tk.Label(window, text="Введіть кількість оцінок для оного учня, щоб згенерувати статистику. Максимальна допустима кількість - 20", font=("Arial", 16)).pack(pady = 20)
entry = tk.Entry(window, width=20, font=("Arial", 14)).pack(pady = 10)
btn = tk.Button(window, text="Сформувати звіт", command=cmn_check).pack(pady = 10)
text = tk.Text(window, height=50, width=300, font=("Arial", 14)).pack(pady = 10)
