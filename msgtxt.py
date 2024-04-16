


import tkinter as tk
import random

# Function to generate a random position for the text
def random_position():
    x = random.randint(0, root.winfo_screenwidth())
    y = random.randint(0, root.winfo_screenheight())
    return (x, y)

# Function to update the text position
def update_text_position():
    x, y = random_position()
    text_label.place(x=x, y=y)
    root.after(100, update_text_position)

# Initialize the tkinter window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')

# Create a label to display the text
text_label = tk.Label(root, text='gsr.exe has ruined your pc.', font=('Arial', 24), fg='white', bg='black')

# Update the text position continuously
update_text_position()

root.mainloop()
