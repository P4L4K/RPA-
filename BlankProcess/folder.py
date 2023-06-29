from PIL import Image, ImageTk
import tkinter as tk

# Function to close the program
def close_program():
    root.destroy()

# Load the image
image_path = r"D:\documents\Documents\UiPath\BlankProcess\folder.png"  # Replace with the actual path to your image file
image = Image.open(image_path)

# Resize the image to a desired width and height
new_width = 800  # Adjust as needed
new_height = 600  # Adjust as needed
image = image.resize((new_width, new_height))

# Create a Tkinter window
root = tk.Tk()

# Set the window title
root.title("Information")

# Set the background color of the window
root.configure(bg="black")

# Convert the image to Tkinter-compatible format
tk_image = ImageTk.PhotoImage(image)

# Create a label and display the image
label = tk.Label(root, image=tk_image)
label.pack()

# Create a frame to hold the button
frame = tk.Frame(root, bg="orange")
frame.pack()

# Create the "Next" button
next_button = tk.Button(frame, text="  Next  ", command=close_program, bg="orange", fg="black")
next_button.pack(side=tk.RIGHT)

# Run the Tkinter event loop
root.mainloop()
