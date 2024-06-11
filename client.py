import tkinter as tk
import socketio

# Connect to the server
sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.event
def message(data):
    messages_list.insert(tk.END, data)

def send_message():
    message = message_entry.get()
    if message:
        sio.send(message)
        message_entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Chat App")

messages_frame = tk.Frame(root)
messages_scrollbar = tk.Scrollbar(messages_frame)

messages_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=messages_scrollbar.set)
messages_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages_list.pack(side=tk.LEFT, fill=tk.BOTH)
messages_list.pack()

messages_frame.pack()

message_entry = tk.Entry(root, width=50)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Connect to the Flask server
sio.connect('http://localhost:5000')

# Start the application
root.mainloop()
