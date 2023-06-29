import tkinter as tk
from PIL import Image, ImageTk

def get_user_input():
    global name
    name = name_entry.get()
    if name:
        message_label.config(text=f'Hello, {name}!')
    else:
        message_label.config(text="Enter the name of drive folder to be created for assignment submission:")
    root.destroy()  # Close the window

def hello():
    return name

root = tk.Tk()
root.title("Assignment folder name")

# Customize the window's appearance and size
root.geometry("1100x800")
root.configure(bg="black")

# Load and display the background image
image_path = r"D:\documents\Documents\UiPath\BlankProcess\QUESTION.png"
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a label to display the message
message_label = tk.Label(root, text="Enter the name of drive folder\n[to be created for assignment submission]", font=("Arial", 16), bg="blue")
message_label.pack(pady=50)

# Add an entry for user input
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(pady=10)

# Add a button to submit the input
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=get_user_input)
submit_button.pack(pady=40)

# Run the event loop to display the window
root.mainloop()

result = hello()
print(result)
