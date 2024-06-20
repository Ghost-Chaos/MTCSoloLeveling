import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

quests = {
    "Sum of Two Numbers": {
        "description": "Write a function to return the sum of two numbers.",
        "input": "(3, 5)",
        "output": "8",
        "points": 10,
        "template": "def sum(a, b):\n    # Write your code here\n    pass"
    },
    "Square of a Number": {
        "description": "Write a function to return the square of a number.",
        "input": "(4,)",
        "output": "16",
        "points": 20,
        "template": "def square(n):\n    # Write your code here\n    pass"
    },
    "Reverse a String": {
        "description": "Write a function to return the reverse of a string.",
        "input": "('hello',)",
        "output": "'olleh'",
        "points": 15,
        "template": "def reverse(s):\n    # Write your code here\n    pass"
    },
    "Prime": {
        "description": "Write a function to check if a number is prime.",
        "input": "(7,)",
        "output": "True",
        "points": 25,
        "template": "def prime(n):\n    # Write your code here\n    pass"
    },
    "Fibonacci Sequence": {
        "description": "Write a function to return the nth Fibonacci number.",
        "input": "(10,)",
        "output": "55",
        "points": 35,
        "template": "def fibonacci(n):\n    # Write your code here\n    pass"
    },
    "Palindrome Check": {
        "description": "Write a function to check if a string is a palindrome.",
        "input": "('racecar',)",
        "output": "True",
        "points": 20,
        "template": "def palindrome(s):\n    # Write your code here\n    pass"
    },
    "Find Maximum in List": {
        "description": "Write a function to find the maximum number in a list.",
        "input": "([1, 2, 3, 4, 5],)",
        "output": "5",
        "points": 20,
        "template": "def find(lst):\n    # Write your code here\n    pass"
    },
    "Vowels": {
        "description": "Write a function to count the number of vowels in a string.",
        "input": "('hello world',)",
        "output": "3",
        "points": 15,
        "template": "def vowels(s):\n    # Write your code here\n    pass"
    },
    "Merge Two Sorted Lists": {
        "description": "Write a function to merge two sorted lists into one sorted list.",
        "input": "([1, 3, 5], [2, 4, 6])",
        "output": "[1, 2, 3, 4, 5, 6]",
        "points": 30,
        "template": "def merge(lst1, lst2):\n    # Write your code here\n    pass"
    }
}

perks = {
    "Double Points": {
        "description": "Double the points earned for each correct solution.",
        "cost": 50
    },
    "Skip Problem": {
        "description": "Skip the current problem and move to the next one.",
        "cost": 20
    }
}

points = 0

def run_code():
    global points
    quest_name = quest_select.get()
    if not quest_name:
        messagebox.showerror("Error", "Please select a quest.")
        return
    
    code = code_editor.get("1.0", tk.END)
    if not code.strip():
        messagebox.showerror("Error", "Please write some code.")
        return

    input_data = quests[quest_name]["input"]
    expected_output = quests[quest_name]["output"]
    points_earned = quests[quest_name]["points"]

    try:
        
        local_namespace = {}
        
        exec(code, {}, local_namespace)

        function_name = quest_name.split()[0].lower() 
        result = eval(f"local_namespace['{function_name}']{input_data}")

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(result))
       
        if str(result) == expected_output:
            messagebox.showinfo("Well done!", f"Your solution is correct! Earned {points_earned} points.")
            points += points_earned
            update_points_label()
        else:
            messagebox.showerror("bruh!", "Your solution is incorrect.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def buy_perk(perk_name):
    global points
    perk_cost = perks[perk_name]["cost"]
    if points >= perk_cost:
        points -= perk_cost
        update_points_label()
        messagebox.showinfo("Rank levelled up", f"You have purchased '{perk_name}'.")
       
    else:
        messagebox.showerror("You got low points", "Gain more points to purchase")

def update_points_label():
    points_label.config(text=f"Points: {points}")

root = tk.Tk()
root.title("Solo Leveling Coding Competition")

quest_select = ttk.Combobox(root, values=list(quests.keys()), state="readonly")
quest_select.pack(pady=10)

quest_description = tk.Text(root, height=3, width=50, state=tk.DISABLED, wrap=tk.WORD)
quest_description.pack(pady=10)

code_editor = tk.Text(root, height=15, width=70)
code_editor.pack(pady=10)

arise_button = ttk.Button(root, text="Arise", command=run_code)
arise_button.pack(pady=10)

output_text = tk.Text(root, height=3, width=70, state=tk.DISABLED)
output_text.pack(pady=10)

points_label = tk.Label(root, text=f"Mana: {points}")
points_label.pack(pady=10)

perks_frame = ttk.LabelFrame(root, text="Perks")
perks_frame.pack(pady=10)

for perk_name, perk_info in perks.items():
    perk_description = perk_info["description"]
    perk_cost = perk_info["cost"]
    perk_button = ttk.Button(perks_frame, text=f"{perk_name} ({perk_cost} points)", 
                             command=lambda p=perk_name: buy_perk(p))
    perk_button.pack(pady=5)

def on_quest_select(event):
    quest_name = quest_select.get()
    quest_description.config(state=tk.NORMAL)
    quest_description.delete("1.0", tk.END)
    quest_description.insert(tk.END, quests[quest_name]["description"])
    quest_description.config(state=tk.DISABLED)
    code_editor.delete("1.0", tk.END)
    code_editor.insert(tk.END, quests[quest_name]["template"])

quest_select.bind("<<ComboboxSelected>>", on_quest_select)

root.mainloop()
