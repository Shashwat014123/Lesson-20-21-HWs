import tkinter as tk
from tkinter import messagebox
import csv

root = tk.Tk()
root.title("Shopping List")
root.geometry("500x500")
root.config(bg="lightblue")

def add_item():
    item = entry.get().strip()

    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter an item!")

def delete_item():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Select an item!")

def save_list():
    with open("shopping_list.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for item in listbox.get(0, tk.END):
            writer.writerow([item])

    messagebox.showinfo("Saved", "Shopping list saved!")

def load_list():
    try:
        listbox.delete(0, tk.END)

        with open("shopping_list.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    listbox.insert(tk.END, row[0])

        messagebox.showinfo("Loaded", "Shopping list loaded!")

    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved shopping list found!")



entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

tk.Button(root, text="Add Item", command=add_item).pack(pady=5)

tk.Button(root, text="Delete Item", command=delete_item).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10)
listbox.pack(pady=15)

tk.Button(root, text="Save List", command=save_list).pack(pady=5)

tk.Button(root, text="Load List", command=load_list).pack(pady=5)

root.mainloop()