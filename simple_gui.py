import tkinter as tk

def on_submit():
    # Get the text from the entry field
    text = entry.get()
    
    # Print the text to the console (you can replace this with your own logic)
    print(f"You entered: {text}")
    
    # Clear the entry field
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple GUI Example")

# Create a label
label = tk.Label(window, text="Enter some text:")
label.pack(pady=20)

# Create an entry field
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button that triggers the on_submit function
button = tk.Button(window, text="Submit", command=on_submit)
button.pack(pady=20)

# Start the main loop
window.mainloop()

