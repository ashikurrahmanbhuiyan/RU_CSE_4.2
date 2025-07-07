import tkinter as tk
import time

def display_name():
    name = "ASHIKUR RAHMAN"  # Replace with your actual name
    for i in range(len(name)):
        label.config(text=name[:i+1])
        root.update()
        time.sleep(0.2)  # Delay between each letter appearing

    # Pause before removing
    time.sleep(1)

    # Remove one letter at a time
    for i in range(len(name), -1, -1):
        label.config(text=name[:i])
        root.update()
        time.sleep(0.2)  # Delay between each letter disappearing

    # Restart the animation
    root.after(1000, display_name)  # Wait 1 second before restarting
    # exit()

# Create the main window
root = tk.Tk()
root.title("Name Animation")
root.geometry("600x600")  # Set window size to 600x600

# Create a label to display the name, centered
label = tk.Label(root, text="", font=("Arial", 36))  # Change "Arial" to desired font, 36 is font size
label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label in the window

# Start the animation
root.after(1000, display_name)  # Start after 1 second

# Run the application
root.mainloop()