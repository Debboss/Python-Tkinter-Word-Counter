import tkinter as tk

def word_counter():
    # Retrieve the text from the entry widget
    text = entry.get()

    # Remove whitespaces
    text = text.strip()

    # If the text is empty, then it returns zero words
    if len(text) == 0:
        label["text"] = "Word count: 0"
        return

    # Split the text into words using whitespace as the delimiter
    words = text.split()

    # Update the label with the word count
    label["text"] = "Word count: " + str(len(words))

# Create the main window
window = tk.Tk()
window.title("Word Counter")
window.geometry("400x200")
window.configure(bg="#ECECEC")  # Set background color

# custom font
font_style = ("Arial", 12)

# Create an entry widget for the user to enter text
entry = tk.Entry(window, width=30, font=font_style, bg="#FFFFFF")
entry.pack(pady=10)

# Create a button to trigger the word counting
button = tk.Button(window, text="Count Words", font=font_style, command=word_counter, bg="#0066CC", fg="#FFFFFF")
button.pack()

# Create a label to display the word count
label = tk.Label(window, text="Word count: 0", font=font_style, bg="#ECECEC")
label.pack(pady=10)

# Start the main event loop
window.mainloop()
