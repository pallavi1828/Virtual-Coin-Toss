import random
import tkinter as tk
from tkinter import messagebox
import time
import math

def coin_toss():
    """Simulate a coin toss and return 'Heads' or 'Tails'."""
    return random.choice(["Heads", "Tails"])

def update_history(history, heads, tails):
    """Store session results in history."""
    history.append((heads, tails))

def show_summary(history):
    """Display all past coin flip sessions."""
    if not history:
        messagebox.showinfo("Session Summary", "No history available yet.")
        return

    summary = "\n📜 Historical Results:\n"
    for i, (heads, tails) in enumerate(history, start=1):
        summary += f"Session {i}: Heads = {heads}, Tails = {tails}\n"

    messagebox.showinfo("Session Summary", summary)

def animate_realistic_coin(canvas, flips, history, result_label):
    """Run animation for coin flipping and display results."""
    heads_count = 0
    tails_count = 0

    for _ in range(flips):
        result = coin_toss()

        # Coin flip animation
        for angle in range(0, 360, 10):
            x_offset = int(50 * math.sin(math.radians(angle)))
            y_offset = int(-30 * math.cos(math.radians(angle)))

            side = "Heads" if angle < 180 else result

            canvas.coords("coin", 150 + x_offset, 100 + y_offset)
            canvas.itemconfig("coin", text=side, font=("Arial", 24, "bold"))

            canvas.update()
            time.sleep(0.03)

        # Final coin result
        canvas.itemconfig("coin", text=result, font=("Arial", 32, "bold"))
        canvas.coords("coin", 150, 100)

        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    total = heads_count + tails_count

    if total == 0:  # Prevent division by zero
        heads_percentage = tails_percentage = 0
    else:
        heads_percentage = (heads_count / total) * 100
        tails_percentage = (tails_count / total) * 100

    # Update history with this session
    update_history(history, heads_count, tails_count)

    # Update results label
    result_text = (
        f"Total Flips: {total}\n"
        f"Heads: {heads_count} ({heads_percentage:.2f}%)\n"
        f"Tails: {tails_count} ({tails_percentage:.2f}%)"
    )

    result_label.config(text=result_text)

def start_toss(entry, history, result_label, canvas):
    """Start the coin flipping process when user enters a number."""
    try:
        flips = int(entry.get())
        if flips <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number.")
            return
        animate_realistic_coin(canvas, flips, history, result_label)
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid number.")

def main():
    """Main Tkinter GUI setup."""
    history = []

    root = tk.Tk()
    root.title("Realistic Coin Toss Simulator")
    root.configure(bg="#f0f8ff")

    tk.Label(root, text="🪙 Realistic Coin Toss Simulator 🪙",
             font=("Arial", 18, "bold"), bg="#f0f8ff").pack(pady=10)

    tk.Label(root, text="Enter the number of tosses:",
             bg="#f0f8ff", font=("Arial", 12)).pack()

    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)

    canvas = tk.Canvas(root, width=400, height=300, bg="#dbeafe",
                       highlightthickness=2, highlightbackground="#4682b4")
    canvas.pack(pady=10)

    canvas.create_text(150, 100, text="", font=("Arial", 32, "bold"), tags="coin")

    result_label = tk.Label(root, text="", font=("Arial", 14),
                            justify="left", bg="#f0f8ff")
    result_label.pack(pady=10)

    tk.Button(root, text="Toss Coins",
              command=lambda: start_toss(entry, history, result_label, canvas),
              font=("Arial", 12), bg="#4682b4", fg="white", padx=10, pady=5).pack(pady=5)

    tk.Button(root, text="Show History",
              command=lambda: show_summary(history),
              font=("Arial", 12), bg="#4682b4", fg="white", padx=10, pady=5).pack(pady=5)

    tk.Button(root, text="Exit",
              command=root.quit, font=("Arial", 12), bg="#ff6347",
              fg="white", padx=10, pady=5).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
