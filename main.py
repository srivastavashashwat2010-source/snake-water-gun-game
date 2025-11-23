import random
import tkinter as tk
from tkinter import ttk, messagebox

CHOICES = {"s": 1, "w": -1, "g": 0}
REVERSE = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}

def decide(user, comp):
    if user == comp:
        return "draw"

    if comp == -1 and user == 1:
        return "win"
    if comp == -1 and user == 0:
        return "lose"
    if comp == 1 and user == -1:
        return "lose"
    if comp == 1 and user == 0:
        return "win"
    if comp == 0 and user == -1:
        return "win"
    if comp == 0 and user == 1:
        return "lose"

    return "error"


class You(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake • Water • Gun")
        self.geometry("520x380")
        self.configure(bg="#f5f7fa")
        self.resizable(False, False)

        self.your_score = 0
        self.comp_score = 0

        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(self, text="Let's Play!", font=("Helvetica", 20, "bold"),
                 bg="#f5f7fa", fg="#333").pack(pady=10)

        # Small intro message
        self.info = tk.Label(self, text="Choose Snake, Water or Gun 😊",
                             font=("Helvetica", 12), bg="#f5f7fa", fg="#444")
        self.info.pack()

        # Buttons
        btn_frame = tk.Frame(self, bg="#f5f7fa")
        btn_frame.pack(pady=18)

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)

        ttk.Button(btn_frame, text="Snake 🐍", command=lambda: self.play(1)).grid(row=0, column=0, padx=12)
        ttk.Button(btn_frame, text="Water 💧", command=lambda: self.play(-1)).grid(row=0, column=1, padx=12)
        ttk.Button(btn_frame, text="Gun 🔫", command=lambda: self.play(0)).grid(row=0, column=2, padx=12)

        # Show choices
        self.choice_label = tk.Label(self, text="", font=("Helvetica", 12),
                                     bg="#f5f7fa", fg="#333")
        self.choice_label.pack(pady=5)

        # Result
        self.result_label = tk.Label(self, text="", font=("Helvetica", 16, "bold"),
                                     bg="#f5f7fa", fg="#444")
        self.result_label.pack(pady=8)

        # Score
        self.score_label = tk.Label(self, text="Score — You: 0 | Computer: 0",
                                    font=("Helvetica", 12), bg="#f5f7fa", fg="#555")
        self.score_label.pack(pady=10)

    def play(self, your_choice):
        comp_choice = random.choice([-1, 0, 1])

       
        self.choice_label.config(
            text=f"You picked {REVERSE[your_choice]} • I picked {REVERSE[comp_choice]}")

        result = decide(your_choice, comp_choice)

        if result == "win":
            self.your_score += 1
            self.result_label.config(text="Nice! You won that round 😄", fg="#16a34a")
        elif result == "lose":
            self.comp_score += 1
            self.result_label.config(text="Oh no… I beat you this time 😅", fg="#dc2626")
        elif result == "draw":
            self.result_label.config(text="Haha! We thought the same 🤝", fg="#ca8a04")
        else:
            self.result_label.config(text="Hmm… something feels off 🤔", fg="#444")

        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=f"Score — You: {self.your_score} | Computer: {self.comp_score}"
        )


if __name__ == "__main__":
    app = You()
    app.mainloop()
