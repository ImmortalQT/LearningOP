import tkinter as tk
from tkinter import scrolledtext
import openai

# Initialize OpenAI with your API key
openai.api_key = 'your-openai-api-key'

def get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_history.insert(tk.END, "ChatGPT: " + response + "\n")
    chat_history.config(state=tk.DISABLED)
    input_box.delete("1.0", tk.END)

def on_enter_press(event):
    send_message()

# Creating the main window
root = tk.Tk()
root.title("ChatGPT App")
root.geometry("600x400")

# Chat history text area (non-editable)
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input text box
input_box = tk.Text(root, height=3)
input_box.pack(padx=10, pady=10, fill=tk.X)
input_box.bind("<Return>", on_enter_press)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the main application loop
root.mainloop()