import tkinter as tk
from PIL import Image, ImageTk

def get_user_input():
    global name
    name = name_entry.get()
    if name:
        message_label.config(text=f'Hello, {name}!')
    else:
        message_label.config(text="Please enter your name.")
    root.destroy()  # Close the window

def hello():
    return name

root = tk.Tk()
root.title("Custom Dialog Box")

# Customize the window's appearance and size
root.geometry("400x300")
root.configure(bg="white")

# Load and display the background image
image_path = r"C:\Users\hp\Downloads\_ecefca38-64f6-4d93-8294-e5cdae3d1e8b.jpeg"
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a label to display the message
message_label = tk.Label(root, text="What is your name?", font=("Arial", 16), bg="white")
message_label.pack(pady=50)

# Add an entry for user input
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=10)

# Add a button to submit the input
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=get_user_input)
submit_button.pack(pady=10)

# Run the event loop to display the window
root.mainloop()

result = hello()
print(result)
